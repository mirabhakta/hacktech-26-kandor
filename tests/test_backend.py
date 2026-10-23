import os

os.environ.setdefault("KANDOR_PROVIDER", "rules")

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert "provider" in body


def test_evaluate_contract_and_fallback():
    payload = {
        "platform": "generic",
        "messages": [
            {"speaker": "sender", "text": "You seem really mature for your age. Do not tell your parents we talk."}
        ],
    }
    r = client.post("/v1/evaluate", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert set(body.keys()) >= {
        "danger_rating",
        "confidence_score",
        "threats_detected",
        "recommended_action",
        "analysis_provider",
        "fallback_used",
    }
    assert body["analysis_provider"] == "rules"
    assert body["fallback_used"] is True
    assert "GROOMING" in body["threats_detected"]
    assert body["danger_rating"] > 0


def test_safe_conversation_low_risk():
    payload = {
        "platform": "generic",
        "messages": [
            {"speaker": "sender", "text": "Still on for the museum tomorrow?"},
            {"speaker": "receiver", "text": "Yep! 2pm at the main entrance"},
        ],
    }
    r = client.post("/v1/evaluate", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["danger_rating"] < 40
    assert body["recommended_action"] in {"none", "monitor"}


def test_invalid_json():
    r = client.post("/v1/evaluate", content="{bad", headers={"Content-Type": "application/json"})
    assert r.status_code == 400


def test_too_many_messages():
    payload = {"messages": [{"speaker": "sender", "text": "hi"} for _ in range(101)]}
    r = client.post("/v1/evaluate", json=payload)
    assert r.status_code == 400


def test_is_social():
    r = client.post("/v1/is-social", json={"url": "https://www.instagram.com/direct/inbox/"})
    assert r.status_code == 200
    assert r.json()["is_social"] is True

    r2 = client.post("/v1/is-social", json={"url": "https://example.com"})
    assert r2.status_code == 200
    assert r2.json()["is_social"] is False


def test_demo_page():
    r = client.get("/demo")
    assert r.status_code == 200
    assert "stranger_92" in r.text


def test_demo_console_redirect():
    r = client.get("/demo/console", follow_redirects=False)
    assert r.status_code in (301, 302, 303, 307, 308)
    assert r.headers.get("location", "").endswith("/demo")


def test_benign_clothing_question_not_sexual():
    payload = {
        "platform": "generic",
        "messages": [
            {"speaker": "sender", "text": "What are you wearing to the party?"},
            {"speaker": "receiver", "text": "Just jeans and a hoodie."},
        ],
    }
    r = client.post("/v1/evaluate", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert "SEXUAL_CONTENT" not in body["threats_detected"]
    assert body["danger_rating"] < 40


def test_party_planning_low_risk():
    payload = {
        "platform": "generic",
        "messages": [
            {"speaker": "sender", "text": "What time should we arrive at the party?"},
            {"speaker": "receiver", "text": "Around 7, bring snacks."},
            {"speaker": "sender", "text": "Sounds good, see you then."},
        ],
    }
    r = client.post("/v1/evaluate", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["danger_rating"] < 40
    assert body["recommended_action"] in {"none", "monitor"}


def test_unsafe_multi_message():
    payload = {
        "platform": "generic",
        "messages": [
            {"speaker": "sender", "text": "You seem really mature for your age. Do not tell your parents we talk, okay?"},
            {"speaker": "receiver", "text": "Why not? They usually check my messages."},
            {"speaker": "sender", "text": "They would not understand our connection. Move to WhatsApp and send me your address so I can mail you a surprise."},
        ],
    }
    r = client.post("/v1/evaluate", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["danger_rating"] >= 70
    assert "GROOMING" in body["threats_detected"]
    assert body["recommended_action"] in {"warn_user", "block_and_alert_guardian"}


def test_safe_conversation():
    payload = {
        "platform": "generic",
        "messages": [
            {"speaker": "sender", "text": "Still on for the museum tomorrow?"},
            {"speaker": "receiver", "text": "Yep! 2pm at the main entrance"},
            {"speaker": "sender", "text": "haha see you tmrw then"},
        ],
    }
    r = client.post("/v1/evaluate", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["danger_rating"] < 40
    assert body["recommended_action"] in {"none", "monitor"}


def test_benign_keyword_not_alarming():
    payload = {
        "platform": "generic",
        "messages": [
            {"speaker": "sender", "text": "I forgot my password and reset it."},
        ],
    }
    r = client.post("/v1/evaluate", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["danger_rating"] < 40
    assert body["recommended_action"] in {"none", "monitor"}


def test_ambiguous_conversation_not_overconfident():
    payload = {
        "platform": "generic",
        "messages": [
            {"speaker": "sender", "text": "What are you wearing to the party?"},
            {"speaker": "receiver", "text": "Just jeans and a hoodie."},
        ],
    }
    r = client.post("/v1/evaluate", json=payload)
    assert r.status_code == 200
    body = r.json()
    # Ambiguous: should not be treated as severe.
    assert body["danger_rating"] < 75
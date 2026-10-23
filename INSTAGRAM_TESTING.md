# Instagram Integration Testing

## Synthetic fixture

`tests/instagram_fixture.html` mimics a simplified Instagram DM layout. `tests/instagram_extraction.mjs` verifies extraction of three messages and exclusion of sidebar content.

## Selectors and assumptions

- Root: `[role='main']` or `main`.
- Message leaves: `[dir='auto']` nodes without nested `[dir='auto']`.
- Sender/receiver inferred from aria labels containing "you sent" / "sent by", or horizontal position.
- Sidebar/thread-list nodes excluded via `a[href*='/direct/t/']` and nav/aside/header.
- UI chrome filtered by `isLikelyInstagramUiChromeText`.

## Authorized live testing steps

1. Use a test Instagram account and a conversation you own or are authorized to inspect.
2. Load the unpacked extension.
3. Open the Instagram DM thread in Chrome.
4. Open the extension popup and click "Scan tab now".
5. Confirm the banner/popup show expected risk and flagged messages.
6. Record any selector drift or false extraction in an issue.

This synthetic fixture does not prove live Instagram compatibility.
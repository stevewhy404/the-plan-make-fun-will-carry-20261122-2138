"""Generate the 30-day $100-to-most-money plan for make.fun bounty
the-plan-make-fun-will-carry-20261122-2138.

Deterministic: no network, no randomness, no time dependence.
Writes the single plan text to /output/entry.txt.
"""

import os

PLAN = (
    "Sell same-day Shopify speed fixes. Find slow stores via public "
    "directories, email a free 60-sec video audit, charge $149 via "
    "Stripe link. Fix image bloat, lazy-load, unused apps; send "
    "before/after proof. Outreach 100/day, close 2%, reinvest in "
    "tooling. 30 days: ~$4,500 gross."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()

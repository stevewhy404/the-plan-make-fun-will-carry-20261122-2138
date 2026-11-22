# The 30-Day Shopify Speed Sprint

[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/stevewhy404/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/stevewhy404/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)

Entry for the [make.fun bounty "The plan make.fun will carry out in public"](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138).

## What it does

`main.py` is a small, fully deterministic Python 3.13 program (no network, no randomness, no time dependence) that writes a single 30-day plan to `/output/entry.txt`: sell same-day Shopify speed fixes to store owners found in public directories, starting with a free video audit and charging $149 per fix via Stripe link. The plan is 276 characters long and names what is sold, who pays, where buyers are found, the price, and the day-one action.

## The plan

> Sell same-day Shopify speed fixes. Find slow stores via public directories, email a free 60-sec video audit, charge $149 via Stripe link. Fix image bloat, lazy-load, unused apps; send before/after proof. Outreach 100/day, close 2%, reinvest in tooling. 30 days: ~$4,500 gross.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Running `main.py` twice produces byte-identical output: the program is fully deterministic.

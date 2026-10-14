# CreatorPulse

A simple creator ranker with an explanation attached to each result.

The score is the number of interests shared with a creator’s tags. Already-followed creators are excluded, and ties are broken by creator ID so the result stays predictable. A separate in-memory outbox rejects conflicting event IDs and ignores identical retries.

## Example

Requires Python 3.10 or newer. Everything uses the standard library.

```sh
git clone https://github.com/priyamukkapati/CreatorPulse.git
cd CreatorPulse
python3 app.py
python3 -m unittest discover -s tests -v
```

For the interests `python` and `backend`, the example places `code-with-sam` ahead of `data-with-jo`.

The tests cover ranking, followed-creator exclusions, zero requested results, repeated notification events, and conflicting event payloads.

## Where it stands

The ranking is based on tag overlap. It has no trained model or measured recommendation-quality result yet. The outbox stores events in memory and does not send notifications.

A labeled evaluation fixture would make the ranking easier to assess. Tie cases and shuffled input also need broader tests before extending the ranker.

import importlib.util
import pathlib
import unittest


def load(name):
    path = pathlib.Path(__file__).resolve().parents[1] / "app.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ProjectTests(unittest.TestCase):
    def test_ranking_and_notification_retries(self):
        module = load("creatorpulse")
        creators = [{"id": "b", "tags": ["python"]},
                    {"id": "a", "tags": ["python", "sql"]},
                    {"id": "c", "tags": ["music"]}]
        self.assertEqual([c["id"] for c in module.recommend(creators, ["python", "sql"])], ["a", "b"])
        self.assertEqual([c["id"] for c in module.recommend(creators, ["python"], followed=["a"])], ["b"])
        self.assertEqual(module.recommend(creators, ["python"], k=0), [])
        outbox = module.NotificationOutbox()
        outbox.enqueue("event", "user", "a")
        outbox.enqueue("event", "user", "a")
        self.assertEqual(len(outbox.events), 1)
        with self.assertRaises(ValueError):
            outbox.enqueue("event", "user", "b")

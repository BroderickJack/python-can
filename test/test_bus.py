from unittest.mock import patch

import can


def test_bus_ignore_config():
    with patch.object(
        target=can.util, attribute="load_config", side_effect=can.util.load_config
    ):
        _ = can.Bus(interface="virtual", ignore_config=True)
        assert not can.util.load_config.called

        _ = can.Bus(interface="virtual")
        assert can.util.load_config.called

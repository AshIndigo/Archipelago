from test.bases import WorldTestBase


class MyGameTestBase(WorldTestBase):
    game = "Devil May Cry 3"


class TestChestAccess(MyGameTestBase):
    def test_sword_chests(self) -> None:
        """Test locations that require a sword"""
        locations = ["Chest1", "Chest2"]
        items = [["Sword"]]
        # this will test that each location can't be accessed without the "Sword", but can be accessed once obtained
        self.assertAccessDependency(locations, items)

    def test_any_weapon_chests(self) -> None:
        """Test locations that require any weapon"""
        locations = [f"Chest{i}" for i in range(3, 6)]
        items = [["Sword"], ["Axe"], ["Spear"]]
        # this will test that chests 3-5 can't be accessed without any weapon, but can be with just one of them
        self.assertAccessDependency(locations, items)
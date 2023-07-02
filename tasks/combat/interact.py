from tasks.base.ui import UI
from tasks.combat.assets.assets_combat_interact import DUNGEON_COMBAT_INTERACT


class CombatInteract(UI):
    def handle_combat_interact(self):
        """
        Returns:
            bool: If clicked.
        """
        return bool(self.appear_then_click(DUNGEON_COMBAT_INTERACT, interval=2))

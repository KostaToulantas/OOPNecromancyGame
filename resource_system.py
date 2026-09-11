class ResourceSystem:
    """Stores and manages summoning resources."""

    # Task 2.7: Constant representing the minimum valid resource quantity.
    MINIMUM_VALID_RESOURCE_QUANTITY = 0

    def __init__(self, necrotic_runes=MINIMUM_VALID_RESOURCE_QUANTITY,
                 spirit_runes=MINIMUM_VALID_RESOURCE_QUANTITY,
                 bone_runes=MINIMUM_VALID_RESOURCE_QUANTITY,
                 flesh_runes=MINIMUM_VALID_RESOURCE_QUANTITY,
                 ectoplasm=MINIMUM_VALID_RESOURCE_QUANTITY):
        # Task 2.1 and Task 2.2: Store the five resources privately as integers.
        # If any starting amount is invalid, every resource begins at 0.
        if self.__is_valid_resource_collection(
            necrotic_runes,
            spirit_runes,
            bone_runes,
            flesh_runes,
            ectoplasm,
        ):
            self.__necrotic_runes = necrotic_runes
            self.__spirit_runes = spirit_runes
            self.__bone_runes = bone_runes
            self.__flesh_runes = flesh_runes
            self.__ectoplasm = ectoplasm
        else:
            self.__necrotic_runes = self.MINIMUM_VALID_RESOURCE_QUANTITY
            self.__spirit_runes = self.MINIMUM_VALID_RESOURCE_QUANTITY
            self.__bone_runes = self.MINIMUM_VALID_RESOURCE_QUANTITY
            self.__flesh_runes = self.MINIMUM_VALID_RESOURCE_QUANTITY
            self.__ectoplasm = self.MINIMUM_VALID_RESOURCE_QUANTITY

    # Task 2.3: Getter methods used by read-only properties.
    def get_necrotic_runes(self):
        return self.__necrotic_runes

    def get_spirit_runes(self):
        return self.__spirit_runes

    def get_bone_runes(self):
        return self.__bone_runes

    def get_flesh_runes(self):
        return self.__flesh_runes

    def get_ectoplasm(self):
        return self.__ectoplasm

    # Task 2.3: Read-only properties using the property() function.
    necrotic_runes = property(get_necrotic_runes)
    spirit_runes = property(get_spirit_runes)
    bone_runes = property(get_bone_runes)
    flesh_runes = property(get_flesh_runes)
    ectoplasm = property(get_ectoplasm)

    def collect_resources(
        self,
        necrotic_runes,
        spirit_runes,
        bone_runes,
        flesh_runes,
        ectoplasm,
    ):
        # Task 2.4: Validate all collected quantities before changing state.
        if not self.__is_valid_resource_collection(
            necrotic_runes,
            spirit_runes,
            bone_runes,
            flesh_runes,
            ectoplasm,
        ):
            return False

        self.__necrotic_runes += necrotic_runes
        self.__spirit_runes += spirit_runes
        self.__bone_runes += bone_runes
        self.__flesh_runes += flesh_runes
        self.__ectoplasm += ectoplasm

        return True

    def has_required_resources(
        self,
        required_necrotic_runes,
        required_spirit_runes,
        required_bone_runes,
        required_flesh_runes,
        required_ectoplasm,
    ):
        # Task 2.5: Check whether all required resources are available.
        if not self.__is_valid_resource_collection(
            required_necrotic_runes,
            required_spirit_runes,
            required_bone_runes,
            required_flesh_runes,
            required_ectoplasm,
        ):
            return False

        return (
            self.__necrotic_runes >= required_necrotic_runes
            and self.__spirit_runes >= required_spirit_runes
            and self.__bone_runes >= required_bone_runes
            and self.__flesh_runes >= required_flesh_runes
            and self.__ectoplasm >= required_ectoplasm
        )

    def spend_resources(
        self,
        required_necrotic_runes,
        required_spirit_runes,
        required_bone_runes,
        required_flesh_runes,
        required_ectoplasm,
    ):
        # Task 2.6: Check all requirements before spending any resource.
        if not self.has_required_resources(
            required_necrotic_runes,
            required_spirit_runes,
            required_bone_runes,
            required_flesh_runes,
            required_ectoplasm,
        ):
            return False

        self.__necrotic_runes -= required_necrotic_runes
        self.__spirit_runes -= required_spirit_runes
        self.__bone_runes -= required_bone_runes
        self.__flesh_runes -= required_flesh_runes
        self.__ectoplasm -= required_ectoplasm

        return True

    def __str__(self):
        # Task 2.8: Clearly display the available resources.
        return (
            f"Necrotic Runes: {self.__necrotic_runes}\n"
            f"Spirit Runes: {self.__spirit_runes}\n"
            f"Bone Runes: {self.__bone_runes}\n"
            f"Flesh Runes: {self.__flesh_runes}\n"
            f"Ectoplasm: {self.__ectoplasm}"
        )

    def __is_valid_resource_collection(
        self,
        necrotic_runes,
        spirit_runes,
        bone_runes,
        flesh_runes,
        ectoplasm,
    ):
        # Task 2.2 and 2.4: Each resource quantity must be an integer
        # and cannot be below the minimum valid quantity.
        return (
            type(necrotic_runes) is int
            and type(spirit_runes) is int
            and type(bone_runes) is int
            and type(flesh_runes) is int
            and type(ectoplasm) is int
            and necrotic_runes >= self.MINIMUM_VALID_RESOURCE_QUANTITY
            and spirit_runes >= self.MINIMUM_VALID_RESOURCE_QUANTITY
            and bone_runes >= self.MINIMUM_VALID_RESOURCE_QUANTITY
            and flesh_runes >= self.MINIMUM_VALID_RESOURCE_QUANTITY
            and ectoplasm >= self.MINIMUM_VALID_RESOURCE_QUANTITY
        )


class Undead:
    """Represents an undead creature summoned by the necromancer."""

    # Task 3.3: Constants defining the current stat boundaries.
    MINIMUM_HEALTH = 1
    MAXIMUM_HEALTH = 100
    MINIMUM_POWER = 1
    MAXIMUM_POWER = 100
    MAXIMUM_LEVEL = 10

    # Task 3.4: Constants defining stat growth when levelling.
    HEALTH_GAINED_PER_LEVEL = 10
    POWER_GAINED_PER_LEVEL = 10

    # Task 3.2: Every undead creature begins at Level 1.
    STARTING_LEVEL = 1

    def __init__(self, unit_identifier, name, health, power):
        # The identifier is private because subclasses do not need to change it.
        # The remaining state is protected so inherited behaviour can use it.
        self.__unit_identifier = unit_identifier
        self._name = name
        self._health = self.__limit_health(health)
        self._power = self.__limit_power(power)
        self._level = self.STARTING_LEVEL

    # Task 3.5: Getter methods used by read-only properties.
    def get_unit_identifier(self):
        return self.__unit_identifier

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health

    def get_power(self):
        return self._power

    def get_level(self):
        return self._level

    # Task 3.5: Read-only properties using the property() function.
    unit_identifier = property(get_unit_identifier)
    name = property(get_name)
    health = property(get_health)
    power = property(get_power)
    level = property(get_level)

    def level_up(self):
        # Task 3.6: Prevent the undead from exceeding the maximum level.
        if self._level >= self.MAXIMUM_LEVEL:
            return False

        # Task 3.6: Increase level, health, and power.
        self._level += 1
        self._health += self.HEALTH_GAINED_PER_LEVEL
        self._power += self.POWER_GAINED_PER_LEVEL

        # Task 3.6: Prevent health and power from exceeding maximum values.
        self._health = self.__limit_health(self._health)
        self._power = self.__limit_power(self._power)

        return True

    def command(self):
        """Return behaviour shared by every undead summon."""
        return f"{self._name} awaits its necromancer's command."

    def __str__(self):
        # Task 3.7: Display the identifier, name, level, health, and power.
        return (
            f"Undead ID: {self.__unit_identifier}\n"
            f"Name: {self._name}\n"
            f"Level: {self._level}/{self.MAXIMUM_LEVEL}\n"
            f"Health: {self._health}/{self.MAXIMUM_HEALTH}\n"
            f"Power: {self._power}/{self.MAXIMUM_POWER}"
        )

    def __limit_health(self, health):
        if type(health) is not int:
            return self.MINIMUM_HEALTH

        if health < self.MINIMUM_HEALTH:
            return self.MINIMUM_HEALTH

        if health > self.MAXIMUM_HEALTH:
            return self.MAXIMUM_HEALTH

        return health

    def __limit_power(self, power):
        if type(power) is not int:
            return self.MINIMUM_POWER

        if power < self.MINIMUM_POWER:
            return self.MINIMUM_POWER

        if power > self.MAXIMUM_POWER:
            return self.MAXIMUM_POWER

        return power


class WarriorUndead(Undead):
    """Represents an undead creature specialised for battle."""

    def __init__(self, unit_identifier, name, health, power):
        super().__init__(unit_identifier, name, health, power)

    def command(self):
        parent_command = super().command()
        return f"{parent_command} It raises its weapon, ready for battle."


class CursedUndead(Undead):
    """Represents an undead creature empowered by a curse."""

    def __init__(self, unit_identifier, name, health, power):
        super().__init__(unit_identifier, name, health, power)

    def command(self):
        parent_command = super().command()
        return f"{parent_command} Cursed energy gathers around it."


class SkeletonWarrior(WarriorUndead):
    """A lightly armoured warrior raised from bones."""

    SUMMON_NAME = "Skeleton Warrior"
    MINIMUM_HEALTH = Undead.MINIMUM_HEALTH
    MAXIMUM_HEALTH = Undead.MAXIMUM_HEALTH
    MINIMUM_POWER = Undead.MINIMUM_POWER
    MAXIMUM_POWER = Undead.MAXIMUM_POWER
    STARTING_HEALTH = 30
    STARTING_POWER = 15

    def __init__(self, unit_identifier):
        super().__init__(
            unit_identifier,
            self.SUMMON_NAME,
            self.STARTING_HEALTH,
            self.STARTING_POWER,
        )


class VengefulGhost(CursedUndead):
    """A spirit bound to the world by vengeance."""

    SUMMON_NAME = "Vengeful Ghost"
    MINIMUM_HEALTH = Undead.MINIMUM_HEALTH
    MAXIMUM_HEALTH = Undead.MAXIMUM_HEALTH
    MINIMUM_POWER = Undead.MINIMUM_POWER
    MAXIMUM_POWER = Undead.MAXIMUM_POWER
    STARTING_HEALTH = 20
    STARTING_POWER = 30

    def __init__(self, unit_identifier):
        super().__init__(
            unit_identifier,
            self.SUMMON_NAME,
            self.STARTING_HEALTH,
            self.STARTING_POWER,
        )


class PutridZombie(Undead):
    """A resilient corpse animated by necromancy."""

    SUMMON_NAME = "Putrid Zombie"
    MINIMUM_HEALTH = Undead.MINIMUM_HEALTH
    MAXIMUM_HEALTH = Undead.MAXIMUM_HEALTH
    MINIMUM_POWER = Undead.MINIMUM_POWER
    MAXIMUM_POWER = Undead.MAXIMUM_POWER
    STARTING_HEALTH = 45
    STARTING_POWER = 10

    def __init__(self, unit_identifier):
        super().__init__(
            unit_identifier,
            self.SUMMON_NAME,
            self.STARTING_HEALTH,
            self.STARTING_POWER,
        )

    def command(self):
        parent_command = super().command()
        return f"{parent_command} It shambles forward relentlessly."


class PhantomGuardian(WarriorUndead):
    """A powerful spectral warrior summoned to guard its master."""

    SUMMON_NAME = "Phantom Guardian"
    MINIMUM_HEALTH = Undead.MINIMUM_HEALTH
    MAXIMUM_HEALTH = Undead.MAXIMUM_HEALTH
    MINIMUM_POWER = Undead.MINIMUM_POWER
    MAXIMUM_POWER = Undead.MAXIMUM_POWER
    STARTING_HEALTH = 60
    STARTING_POWER = 35

    def __init__(self, unit_identifier):
        super().__init__(
            unit_identifier,
            self.SUMMON_NAME,
            self.STARTING_HEALTH,
            self.STARTING_POWER,
        )


class SummoningRitual:
    """Describes the requirements and result of a summoning ritual."""

    # Task 4.3: Every ritual must require at least this much Ectoplasm.
    MINIMUM_ECTOPLASM_COST = 1

    # Task 4.3: Rune costs can be 0, so this is the minimum Rune cost.
    MINIMUM_RUNE_COST = 0

    def __init__(self, ritual_name, summon_class, necrotic_rune_cost,
                 spirit_rune_cost, bone_rune_cost, flesh_rune_cost,
                 ectoplasm_cost):
        # Task 4.1: Store information about the ritual and its result.
        if not isinstance(summon_class, type) or not issubclass(
            summon_class, Undead
        ):
            raise TypeError("summon_class must inherit from Undead")

        self.__ritual_name = ritual_name
        self.__summon_class = summon_class

        # Task 4.2 and Task 4.3: Store resource requirements.
        self.__necrotic_rune_cost = self.__limit_rune_cost(necrotic_rune_cost)
        self.__spirit_rune_cost = self.__limit_rune_cost(spirit_rune_cost)
        self.__bone_rune_cost = self.__limit_rune_cost(bone_rune_cost)
        self.__flesh_rune_cost = self.__limit_rune_cost(flesh_rune_cost)
        self.__ectoplasm_cost = self.__limit_ectoplasm_cost(ectoplasm_cost)

    # Task 4.4: Getter methods used by read-only properties.
    def get_ritual_name(self):
        return self.__ritual_name

    def get_summon_class(self):
        return self.__summon_class

    def get_undead_name(self):
        return self.__summon_class.SUMMON_NAME

    def get_starting_health(self):
        return self.__summon_class.STARTING_HEALTH

    def get_starting_power(self):
        return self.__summon_class.STARTING_POWER

    def get_necrotic_rune_cost(self):
        return self.__necrotic_rune_cost

    def get_spirit_rune_cost(self):
        return self.__spirit_rune_cost

    def get_bone_rune_cost(self):
        return self.__bone_rune_cost

    def get_flesh_rune_cost(self):
        return self.__flesh_rune_cost

    def get_ectoplasm_cost(self):
        return self.__ectoplasm_cost

    # Task 4.4: Read-only properties using the property() function.
    ritual_name = property(get_ritual_name)
    summon_class = property(get_summon_class)
    undead_name = property(get_undead_name)
    starting_health = property(get_starting_health)
    starting_power = property(get_starting_power)
    necrotic_rune_cost = property(get_necrotic_rune_cost)
    spirit_rune_cost = property(get_spirit_rune_cost)
    bone_rune_cost = property(get_bone_rune_cost)
    flesh_rune_cost = property(get_flesh_rune_cost)
    ectoplasm_cost = property(get_ectoplasm_cost)

    def can_perform(self, resources):
        # Task 4.5: Require a valid resource object before checking costs.
        if not isinstance(resources, ResourceSystem):
            return False

        return resources.has_required_resources(
            self.__necrotic_rune_cost,
            self.__spirit_rune_cost,
            self.__bone_rune_cost,
            self.__flesh_rune_cost,
            self.__ectoplasm_cost,
        )

    def consume_required_resources(self, resources):
        # Task 4.6: Delegate resource spending to the ResourceSystem object.
        if not isinstance(resources, ResourceSystem):
            return False

        return resources.spend_resources(
            self.__necrotic_rune_cost,
            self.__spirit_rune_cost,
            self.__bone_rune_cost,
            self.__flesh_rune_cost,
            self.__ectoplasm_cost,
        )

    def create_undead(self, unit_identifier):
        # Task 4.7: Create the specialised undead selected by this ritual.
        return self.__summon_class(unit_identifier)

    def __str__(self):
        return (
            f"Ritual: {self.__ritual_name}\n"
            f"Creates: {self.__summon_class.SUMMON_NAME}\n"
            f"Starting Health: {self.__summon_class.STARTING_HEALTH}\n"
            f"Starting Power: {self.__summon_class.STARTING_POWER}\n"
            f"Necrotic Rune Cost: {self.__necrotic_rune_cost}\n"
            f"Spirit Rune Cost: {self.__spirit_rune_cost}\n"
            f"Bone Rune Cost: {self.__bone_rune_cost}\n"
            f"Flesh Rune Cost: {self.__flesh_rune_cost}\n"
            f"Ectoplasm Cost: {self.__ectoplasm_cost}"
        )

    def __limit_rune_cost(self, rune_cost):
        if type(rune_cost) is not int:
            return self.MINIMUM_RUNE_COST

        if rune_cost < self.MINIMUM_RUNE_COST:
            return self.MINIMUM_RUNE_COST

        return rune_cost

    def __limit_ectoplasm_cost(self, ectoplasm_cost):
        if type(ectoplasm_cost) is not int:
            return self.MINIMUM_ECTOPLASM_COST

        if ectoplasm_cost < self.MINIMUM_ECTOPLASM_COST:
            return self.MINIMUM_ECTOPLASM_COST

        return ectoplasm_cost

class Necromancer:
    """Coordinates resources, rituals, and controlled undead summons."""

    # Task 1.3: Constant representing the maximum number of controlled undead.
    MAXIMUM_CONTROLLED_UNDEAD = 5

    FIRST_SUMMON_IDENTIFIER = 1

    def __init__(
        self,
        name,
        necrotic_runes=ResourceSystem.MINIMUM_VALID_RESOURCE_QUANTITY,
        spirit_runes=ResourceSystem.MINIMUM_VALID_RESOURCE_QUANTITY,
        bone_runes=ResourceSystem.MINIMUM_VALID_RESOURCE_QUANTITY,
        flesh_runes=ResourceSystem.MINIMUM_VALID_RESOURCE_QUANTITY,
        ectoplasm=ResourceSystem.MINIMUM_VALID_RESOURCE_QUANTITY,
    ):
        # Task 1.1 and 1.2: The Necromancer creates and owns its resources.
        self.__name = name
        self.__resources = ResourceSystem(
            necrotic_runes,
            spirit_runes,
            bone_runes,
            flesh_runes,
            ectoplasm,
        )
        self.__controlled_undead = []
        self.__next_unit_identifier = self.FIRST_SUMMON_IDENTIFIER

    # Task 1.2: Getter methods used by read-only properties.
    def get_name(self):
        return self.__name

    def get_resources(self):
        return self.__resources

    def get_controlled_undead(self):
        return self.__controlled_undead

    def get_next_unit_identifier(self):
        return self.__next_unit_identifier

    name = property(get_name)
    resources = property(get_resources)
    controlled_undead = property(get_controlled_undead)
    next_unit_identifier = property(get_next_unit_identifier)

    def collect_resources(
        self,
        necrotic_runes,
        spirit_runes,
        bone_runes,
        flesh_runes,
        ectoplasm,
    ):
        # Task 1.2: Delegate resource changes to the ResourceSystem object.
        return self.__resources.collect_resources(
            necrotic_runes,
            spirit_runes,
            bone_runes,
            flesh_runes,
            ectoplasm,
        )

    def summon_undead(self, ritual):
        # Task 1.4: Require a SummoningRitual and enough resources.
        if not isinstance(ritual, SummoningRitual):
            return None

        if len(self.__controlled_undead) >= self.MAXIMUM_CONTROLLED_UNDEAD:
            return None

        if not ritual.can_perform(self.__resources):
            return None

        if not ritual.consume_required_resources(self.__resources):
            return None

        undead = ritual.create_undead(self.__next_unit_identifier)
        self.__next_unit_identifier += 1
        self.__controlled_undead.append(undead)

        return undead

    def dismiss_undead(self, unit_identifier):
        # Task 1.5 and 1.6: Use the helper to find and remove a summon.
        undead = self.__find_controlled_summon(unit_identifier)

        if undead is None:
            return False

        self.__controlled_undead.remove(undead)
        return True

    def level_controlled_undead(self, unit_identifier):
        # Task 1.7: Find a summon, then delegate levelling to the undead object.
        undead = self.__find_controlled_summon(unit_identifier)

        if undead is None:
            return False

        return undead.level_up()

    def __str__(self):
        controlled_count = len(self.__controlled_undead)

        return (
            f"Necromancer: {self.__name}\n"
            f"Controlled Undead: {controlled_count}/{self.MAXIMUM_CONTROLLED_UNDEAD}\n"
            f"Next Summon ID: {self.__next_unit_identifier}\n"
            f"Resources:\n{self.__resources}"
        )

    def __find_controlled_summon(self, unit_identifier):
        # Task 1.6: Private helper for locating controlled undead by ID.
        for undead in self.__controlled_undead:
            if undead.unit_identifier == unit_identifier:
                return undead

        return None


# Task 4.8: Create at least four ritual objects.
SKELETON_WARRIOR_RITUAL = SummoningRitual(
    "Raise Skeleton Warrior",
    SkeletonWarrior,
    1,
    0,
    3,
    0,
    2,
)

VENGEFUL_GHOST_RITUAL = SummoningRitual(
    "Bind Vengeful Ghost",
    VengefulGhost,
    2,
    4,
    0,
    0,
    3,
)

PUTRID_ZOMBIE_RITUAL = SummoningRitual(
    "Raise Putrid Zombie",
    PutridZombie,
    1,
    0,
    1,
    4,
    2,
)

PHANTOM_GUARDIAN_RITUAL = SummoningRitual(
    "Summon Phantom Guardian",
    PhantomGuardian,
    3,
    5,
    2,
    0,
    5,
)


def display_controlled_undead(necromancer):
    if len(necromancer.controlled_undead) == 0:
        print("No controlled undead.")
    else:
        for undead in necromancer.controlled_undead:
            print(undead)
            print()


necromancer = Necromancer("Morgath", 5, 5, 5, 5, 10)

print("Starting necromancer:")
print(necromancer)

print()
print("Successful summons:")
skeleton = necromancer.summon_undead(SKELETON_WARRIOR_RITUAL)
ghost = necromancer.summon_undead(VENGEFUL_GHOST_RITUAL)
zombie = necromancer.summon_undead(PUTRID_ZOMBIE_RITUAL)

print(skeleton)
print()
print(ghost)
print()
print(zombie)

print()
print("After successful summons:")
print(necromancer)
print()
print(f"Controlled undead count: {len(necromancer.controlled_undead)}")

print()
print("Attempting Phantom Guardian without enough resources:")
resources_before_failed_ritual = str(necromancer.resources)
phantom = necromancer.summon_undead(PHANTOM_GUARDIAN_RITUAL)
resources_after_failed_ritual = str(necromancer.resources)
print(f"Phantom Guardian summoned: {phantom is not None}")
print(
    f"Resources unchanged: {resources_before_failed_ritual == resources_after_failed_ritual}")
print(necromancer.resources)

print()
print("Collecting additional resources:")
necromancer.collect_resources(2, 4, 1, 0, 2)
print(necromancer.resources)

print()
print("Attempting Phantom Guardian again:")
phantom = necromancer.summon_undead(PHANTOM_GUARDIAN_RITUAL)
print(f"Phantom Guardian summoned: {phantom is not None}")
print(phantom)

print()
print("Skeleton before levelling:")
print(skeleton)
necromancer.level_controlled_undead(skeleton.unit_identifier)
print()
print("Skeleton after levelling through the necromancer:")
print(skeleton)

print()
print("Dismissing the Vengeful Ghost:")
dismissed = necromancer.dismiss_undead(ghost.unit_identifier)
print(f"Dismissed: {dismissed}")
print(f"Controlled undead count: {len(necromancer.controlled_undead)}")

print()
print("Final necromancer state:")
print(necromancer)
print()
print("Remaining controlled undead:")
display_controlled_undead(necromancer)

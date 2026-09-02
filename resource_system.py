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
        # Task 3.1: Store the undead identifier, name, health, power, and level as private attributes.
        self.__unit_identifier = unit_identifier
        self.__name = name
        self.__health = self.__limit_health(health)
        self.__power = self.__limit_power(power)
        self.__level = self.STARTING_LEVEL

    # Task 3.5: Getter methods used by read-only properties.
    def get_unit_identifier(self):
        return self.__unit_identifier

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_power(self):
        return self.__power

    def get_level(self):
        return self.__level

    # Task 3.5: Read-only properties using the property() function.
    unit_identifier = property(get_unit_identifier)
    name = property(get_name)
    health = property(get_health)
    power = property(get_power)
    level = property(get_level)

    def level_up(self):
        # Task 3.6: Prevent the undead from exceeding the maximum level.
        if self.__level >= self.MAXIMUM_LEVEL:
            return False

        # Task 3.6: Increase level, health, and power.
        self.__level += 1
        self.__health += self.HEALTH_GAINED_PER_LEVEL
        self.__power += self.POWER_GAINED_PER_LEVEL

        # Task 3.6: Prevent health and power from exceeding maximum values.
        self.__health = self.__limit_health(self.__health)
        self.__power = self.__limit_power(self.__power)

        return True

    def __str__(self):
        # Task 3.7: Display the identifier, name, level, health, and power.
        return (
            f"Undead ID: {self.__unit_identifier}\n"
            f"Name: {self.__name}\n"
            f"Level: {self.__level}/{self.MAXIMUM_LEVEL}\n"
            f"Health: {self.__health}/{self.MAXIMUM_HEALTH}\n"
            f"Power: {self.__power}/{self.MAXIMUM_POWER}"
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


class SummoningRitual:
    """Describes the requirements and result of a summoning ritual."""

    # Task 4.3: Every ritual must require at least this much Ectoplasm.
    MINIMUM_ECTOPLASM_COST = 1

    # Task 4.3: Rune costs can be 0, so this is the minimum Rune cost.
    MINIMUM_RUNE_COST = 0

    def __init__(self, ritual_name, undead_name, starting_health,
                 starting_power, necrotic_rune_cost, spirit_rune_cost,
                 bone_rune_cost, flesh_rune_cost, ectoplasm_cost):
        # Task 4.1: Store information about the ritual and its result.
        self.__ritual_name = ritual_name
        self.__undead_name = undead_name
        self.__starting_health = self.__limit_starting_health(starting_health)
        self.__starting_power = self.__limit_starting_power(starting_power)

        # Task 4.2 and Task 4.3: Store resource requirements.
        self.__necrotic_rune_cost = self.__limit_rune_cost(necrotic_rune_cost)
        self.__spirit_rune_cost = self.__limit_rune_cost(spirit_rune_cost)
        self.__bone_rune_cost = self.__limit_rune_cost(bone_rune_cost)
        self.__flesh_rune_cost = self.__limit_rune_cost(flesh_rune_cost)
        self.__ectoplasm_cost = self.__limit_ectoplasm_cost(ectoplasm_cost)

    # Task 4.4: Getter methods used by read-only properties.
    def get_ritual_name(self):
        return self.__ritual_name

    def get_undead_name(self):
        return self.__undead_name

    def get_starting_health(self):
        return self.__starting_health

    def get_starting_power(self):
        return self.__starting_power

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
        # Task 4.7: Create an Undead using this ritual's summon details.
        return Undead(
            unit_identifier,
            self.__undead_name,
            self.__starting_health,
            self.__starting_power,
        )

    def __str__(self):
        return (
            f"Ritual: {self.__ritual_name}\n"
            f"Creates: {self.__undead_name}\n"
            f"Starting Health: {self.__starting_health}\n"
            f"Starting Power: {self.__starting_power}\n"
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

    def __limit_starting_health(self, starting_health):
        if type(starting_health) is not int:
            return Undead.MINIMUM_HEALTH

        if starting_health < Undead.MINIMUM_HEALTH:
            return Undead.MINIMUM_HEALTH

        if starting_health > Undead.MAXIMUM_HEALTH:
            return Undead.MAXIMUM_HEALTH

        return starting_health

    def __limit_starting_power(self, starting_power):
        if type(starting_power) is not int:
            return Undead.MINIMUM_POWER

        if starting_power < Undead.MINIMUM_POWER:
            return Undead.MINIMUM_POWER

        if starting_power > Undead.MAXIMUM_POWER:
            return Undead.MAXIMUM_POWER

        return starting_power


# Task 4.8: Create at least four ritual objects.
SKELETON_WARRIOR_RITUAL = SummoningRitual(
    "Raise Skeleton Warrior",
    "Skeleton Warrior",
    30,
    15,
    1,
    0,
    3,
    0,
    2,
)

VENGEFUL_GHOST_RITUAL = SummoningRitual(
    "Bind Vengeful Ghost",
    "Vengeful Ghost",
    20,
    30,
    2,
    4,
    0,
    0,
    3,
)

PUTRID_ZOMBIE_RITUAL = SummoningRitual(
    "Raise Putrid Zombie",
    "Putrid Zombie",
    45,
    10,
    1,
    0,
    1,
    4,
    2,
)

PHANTOM_GUARDIAN_RITUAL = SummoningRitual(
    "Summon Phantom Guardian",
    "Phantom Guardian",
    60,
    35,
    3,
    5,
    2,
    0,
    5,
)

resource_1 = ResourceSystem(5, 5, 5, 5, 10)
ritual_1 = SummoningRitual(
    "Summon Zombie Pigman",
    "Zombie Pigman",
    50,
    40,
    4,
    0,
    4,
    5,
    4
)

ritual_2 = SummoningRitual(
    "Summon Wither Skeleton",
    "Wither Skeleton",
    60,
    45,
    4,
    1,
    5,
    0,
    5
)

print(resource_1)

can_perform_1 = ritual_1.can_perform(resource_1)
print(can_perform_1)

can_perform_2 = ritual_2.can_perform(resource_1)
print(can_perform_2)

undead_1 = ritual_1.create_undead(1)
print(undead_1)

print(undead_1)
undead_1.level_up()
print(undead_1)

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

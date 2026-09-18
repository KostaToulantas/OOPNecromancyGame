class ResourceSystem:
    """Stores and manages summoning resources."""

    # Task 2.7: Constant representing the minimum valid resource quantity.
    MINIMUM_VALID_RESOURCE_QUANTITY = 0

    def __init__(self, necrotic_runes=MINIMUM_VALID_RESOURCE_QUANTITY,
                 spirit_runes=MINIMUM_VALID_RESOURCE_QUANTITY,
                 bone_runes=MINIMUM_VALID_RESOURCE_QUANTITY,
                 flesh_runes=MINIMUM_VALID_RESOURCE_QUANTITY,
                 ectoplasm=MINIMUM_VALID_RESOURCE_QUANTITY):
        """Store starting resources, setting all amounts to zero if any amount is invalid."""
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
        """Return the necrotic runes."""
        return self.__necrotic_runes

    def get_spirit_runes(self):
        """Return the spirit runes."""
        return self.__spirit_runes

    def get_bone_runes(self):
        """Return the bone runes."""
        return self.__bone_runes

    def get_flesh_runes(self):
        """Return the flesh runes."""
        return self.__flesh_runes

    def get_ectoplasm(self):
        """Return the ectoplasm."""
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
        """Add non-negative integer amounts; return False without changes if any are invalid."""
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
        """Return whether all costs are non-negative integers covered by available resources."""
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
        """Deduct all costs if affordable and valid; otherwise return False without changes."""
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
        """Return the available quantities of all five resources as formatted text."""
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
        """Return whether every quantity is a non-negative integer, excluding booleans."""
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

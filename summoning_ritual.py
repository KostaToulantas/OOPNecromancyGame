from undead import Undead
from resource_system import ResourceSystem


class SummoningRitual:
    """Describes the requirements and result of a summoning ritual."""

    # Task 4.3: Every ritual must require at least this much Ectoplasm.
    MINIMUM_ECTOPLASM_COST = 1

    # Task 4.3: Rune costs can be 0, so this is the minimum Rune cost.
    MINIMUM_RUNE_COST = 0

    def __init__(
        self,
        ritual_name,
        summon_class,
        necrotic_rune_cost,
        spirit_rune_cost,
        bone_rune_cost,
        flesh_rune_cost,
        ectoplasm_cost,
    ):
        """Store the ritual and bounded costs; raise TypeError if summon_class is not an Undead class."""
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
        """Return the ritual name."""
        return self.__ritual_name

    def get_summon_class(self):
        """Return the class used to create this ritual's summon."""
        return self.__summon_class

    def get_undead_name(self):
        """Return the summon name defined by the selected summon class."""
        return self.__summon_class.SUMMON_NAME

    def get_starting_health(self):
        """Return the starting health defined by the selected summon class."""
        return self.__summon_class.STARTING_HEALTH

    def get_starting_power(self):
        """Return the starting power defined by the selected summon class."""
        return self.__summon_class.STARTING_POWER

    def get_necrotic_rune_cost(self):
        """Return the necrotic rune cost."""
        return self.__necrotic_rune_cost

    def get_spirit_rune_cost(self):
        """Return the spirit rune cost."""
        return self.__spirit_rune_cost

    def get_bone_rune_cost(self):
        """Return the bone rune cost."""
        return self.__bone_rune_cost

    def get_flesh_rune_cost(self):
        """Return the flesh rune cost."""
        return self.__flesh_rune_cost

    def get_ectoplasm_cost(self):
        """Return the ectoplasm cost."""
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
        """Return whether a valid ResourceSystem contains enough resources for this ritual."""
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
        """Spend the ritual costs and return success, or False for invalid or insufficient resources."""
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

    def create_summon(self, unit_identifier):
        """Create this ritual's specialised summon with the supplied ID."""
        return self.__summon_class(unit_identifier)

    def __str__(self):
        """Return the ritual name, summon details, and resource costs as formatted text."""
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
        """Return an integer rune cost of at least zero, using zero for non-integers."""
        if type(rune_cost) is not int:
            return self.MINIMUM_RUNE_COST

        if rune_cost < self.MINIMUM_RUNE_COST:
            return self.MINIMUM_RUNE_COST

        return rune_cost

    def __limit_ectoplasm_cost(self, ectoplasm_cost):
        """Return an integer ectoplasm cost of at least one, using one for non-integers."""
        if type(ectoplasm_cost) is not int:
            return self.MINIMUM_ECTOPLASM_COST

        if ectoplasm_cost < self.MINIMUM_ECTOPLASM_COST:
            return self.MINIMUM_ECTOPLASM_COST

        return ectoplasm_cost

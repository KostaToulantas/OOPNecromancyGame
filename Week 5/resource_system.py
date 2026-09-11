from undead import Undead
from summoning_ritual import SummoningRitual
from necromancer import Necromancer


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
print("Specialised summon type checks and commands:")
expected_summon_types = (
    (skeleton, SkeletonWarrior),
    (ghost, VengefulGhost),
    (zombie, PutridZombie),
    (phantom, PhantomGuardian),
)

for summon, expected_type in expected_summon_types:
    print(
        f"{summon.name}: is Undead = {isinstance(summon, Undead)}, "
        f"is {expected_type.__name__} = {type(summon) is expected_type}"
    )
    print(f"Command: {summon.command()}")

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

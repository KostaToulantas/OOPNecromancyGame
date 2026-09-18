from undead import (
    Undead,
    WarriorUndead,
    CursedUndead,
    DeathKnight,
    SkeletonWarrior,
    VengefulGhost,
    PutridZombie,
    PhantomGuardian,
)
from summoning_ritual import SummoningRitual
from necromancer import Necromancer

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

print()
print("Death Knight multiple-inheritance checks:")
death_knight = DeathKnight(necromancer.next_unit_identifier)
print(death_knight)
print(f"Is WarriorUndead: {isinstance(death_knight, WarriorUndead)}")
print(f"Is CursedUndead: {isinstance(death_knight, CursedUndead)}")
print(f"Is Undead: {isinstance(death_knight, Undead)}")
print(f"Combat style: {death_knight.combat_style()}")
print(f"Command: {death_knight.command()}")

print()
print("Death Knight method resolution order:")
for parent in DeathKnight.__mro__:
    print(parent.__name__)
print(f"Combat style through super(): {death_knight.combat_style()}")
print("WarriorUndead is selected first because it precedes CursedUndead in the MRO.")
print()
print("Explicit parent combat styles:")
print(death_knight.compare_combat_styles())
print("super() follows the MRO. Explicit class calls select the named parent's method.")

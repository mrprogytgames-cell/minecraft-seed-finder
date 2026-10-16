import random
import time
from cubiomespi import Generator, MCVersion, Dimension, BiomeID, Structure, get_spawn_pos, get_biome_at, find_closest_structure

VERSION = MCVersion.MC_1_20
MAX_DIST = 500

gen = Generator(VERSION, 0, Dimension.DIM_OVERWORLD)

def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def check(seed):
    gen.seed = seed
    spawn = get_spawn_pos(gen)

    biome = get_biome_at(gen, spawn[0], 0, spawn[1])
    if biome in (BiomeID.ocean, BiomeID.deep_ocean, BiomeID.frozen_ocean):
        return None

    targets = {
        "village": Structure.Village,
        "portal": Structure.Ruined_Portal,
        "temple": Structure.Desert_Pyramid,
        "mineshaft": Structure.Mineshaft,
    }

    result = {"seed": seed, "spawn": spawn}

    for name, struct in targets.items():
        pos = find_closest_structure(gen, struct, spawn[0], spawn[1], MAX_DIST)
        if pos is None:
            return None
        if dist(spawn, pos) > MAX_DIST:
            return None
        result[name] = pos

    return result

print(f"Searching for an overpowered speedrun seed ({MAX_DIST} blocks around spawn)...")
print("-" * 60)

start = time.time()
attempts = 0

while True:
    seed = random.getrandbits(64) - 2**63
    attempts += 1
    result = check(seed)

    if result:
        print("\n[+] SEED FOUND")
        print(f"    Seed:      {result['seed']}")
        print(f"    Spawn:     {result['spawn']}")
        print(f"    Village:   {result['village']}")
        print(f"    Portal:    {result['portal']}")
        print(f"    Temple:    {result['temple']}")
        print(f"    Mineshaft: {result['mineshaft']}")
        print(f"\n    Attempts:  {attempts:,}")
        print(f"    Time:      {time.time() - start:.1f}s")
        break

    if attempts % 50000 == 0:
        print(f"  ... {attempts:,} checked")
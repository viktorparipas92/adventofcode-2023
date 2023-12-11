import re


def part_one(filename):
    """
    --- Day 5: If You Give A Seed A Fertilizer ---

    The almanac (your puzzle input) lists all the seeds that need to be
    planted.
    It also lists
    - what type of soil to use with each kind of seed,
    - what type of fertilizer to use with each kind of soil,
    - what type of water to use with each kind of fertilizer, and so on.
    Every type of seed, soil, fertilizer and so on is identified with a
    number, but numbers are reused by each category - that is, soil 123 and
    fertilizer 123 aren't necessarily related to each other.

    For example:
    The almanac starts by listing which seeds need to be planted:
    seeds 79, 14, 55, and 13.

    The rest of the almanac contains a list of maps which describe how to
    convert numbers from a source category into numbers in a destination
    category. That is, the section that starts with seed-to-soil map:
    describes how to convert a seed number (the source) to a soil number (the
    destination). This lets the gardener and his team know which soil to use
    with which seeds, which water to use with which fertilizer, and so on.

    Rather than list every source number and its corresponding destination
    number one by one, the maps describe entire ranges of numbers that can be
    converted.
    Each line within a map contains three numbers:
    - the destination range start,
    - the source range start,
    - and the range length.

    Any source numbers that aren't mapped correspond to the same destination
    number. So, seed number 10 corresponds to soil number 10.

    So, the entire list of seed numbers and their corresponding soil numbers
    looks like this:
    With this map, you can look up the soil number required for each initial
    seed number:

    The gardener and his team want to get started as soon as possible,
    so they'd like to know the closest location that needs a seed. Using
    these maps, find the lowest location number that corresponds to any of
    the initial seeds. To do this, you'll need to convert each seed number
    through other categories until you can find its corresponding location number.

    In this example, the corresponding types are:
    Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
    Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
    Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
    Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
    So, the lowest location number in this example is 35.

    What is the lowest location number that corresponds to any of the initial
    seed numbers?
    """
    almanac: Almanac = parse_input(filename)
    locations: list[int] = almanac.get_locations()
    return min(locations)


def parse_input(filename: str):
    with open(filename) as file:
        contents = file.read()

    return Almanac(contents)


class Almanac:
    def __init__(self, contents: str):
        (
            seeds,
            seed_soil_map,
            soil_fertilizer_map,
            fertilizer_water_map,
            water_light_map,
            light_temperature_map,
            temperature_humidity_map,
            humidity_location_map,
        ) = contents.split('\n\n')
        self.seeds = SeedList(seeds)
        self.seed_soil_map = Map(seed_soil_map)
        self.soil_fertilizer_map = Map(soil_fertilizer_map)
        self.fertilizer_water_map = Map(fertilizer_water_map)
        self.water_light_map = Map(water_light_map)
        self.light_temperature_map = Map(light_temperature_map)
        self.temperature_humidity_map = Map(temperature_humidity_map)
        self.humidity_location_map = Map(humidity_location_map)

    def get_locations(self) -> list[int]:
        locations = []
        for seed in self.seeds:
            soil = self.seed_soil_map[seed]
            fertilizer = self.soil_fertilizer_map[soil]
            water = self.fertilizer_water_map[fertilizer]
            light = self.water_light_map[water]
            temperature = self.light_temperature_map[light]
            humidity = self.temperature_humidity_map[temperature]
            location = self.humidity_location_map[humidity]
            locations.append(location)

        return locations


class Map:
    def __init__(self, map_input: str):
        if re.match(r'^\S+-to-\S+ map', map_input):
            map: str = map_input.split(':\n')[1]
            map: list[str] = map.split('\n')
            map: list[tuple] = [
                tuple(line.split()) for line in map
            ]
            self.map: list[tuple] = [
                (int(destination), int(source), int(length))
                for destination, source, length in map
            ]
        else:
            raise ValueError('This is not a valid map.')

    def __getitem__(self, item):
        for destination, source, length in self.map:
            if source <= item < source + length:
                return item - source + destination

        return item


class SeedList:
    def __init__(self, seeds_input: str):
        if seeds_input.startswith('seeds: '):
            seeds: str = seeds_input.split(': ')[1]
            self.seed_list = [int(seed) for seed in seeds.split(' ')]
        else:
            raise ValueError('This is not a valid seed list.')

    def __getitem__(self, item):
        return self.seed_list[item]


if __name__ == '__main__':
    filename = 'input.txt'
    minimum_location = part_one(filename)
    print(minimum_location)

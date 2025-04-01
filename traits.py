import random

schizoid_traits = [
    "Neither desires nor enjoys close relationships, including being part of a family",
    "Almost always chooses solitary activities",
    "Has little, if any, interest in having sexual experiences with another person",
    "Takes pleasure in few, if any, activities",
    "Lacks close friends or confidants other than first-degree relatives",
    "Appears indifferent to the praise or criticism of others",
    "Shows emotional coldness, detachment, or flattened affectivity"
]

narcissistic_traits = [
    "Has a grandiose sense of self-importance",
    "Is preoccupied with fantasies of unlimited success, power, brilliance, beauty, or ideal love",
    "Believes that he or she is 'special' and unique",
    "Requires excessive admiration",
    "Has a sense of entitlement",
    "Is interpersonally exploitative",
    "Lacks empathy; is unwilling to recognize or identify with the feelings and needs of others",
    "Is often envious of others or believes that others are envious of him or her",
    "Shows arrogant, haughty behaviors or attitudes"
]

avoidant_traits = [
    "Avoids occupational activities that involve significant interpersonal contact",
    "Is unwilling to get involved with people unless certain of being liked",
    "Shows restraint within intimate relationships because of the fear of being shamed or ridiculed",
    "Is preoccupied with being criticized or rejected in social situations",
    "Is inhibited in new interpersonal situations because of feelings of inadequacy",
    "Views self as socially inept, personally unappealing, or inferior to others",
    "Is unusually reluctant to take personal risks or to engage in any new activities because they may prove embarrassing"
]

combinations = [[i, j, k] for i in [0, 1] for j in [0, 1] for k in [0, 1]]


def randget_schizoid_trait() -> str:
    n = len(schizoid_traits)
    random_index = random.randint(0, n - 1)
    return schizoid_traits[random_index]


def randget_narci_trait() -> str:
    n = len(narcissistic_traits)
    random_index = random.randint(0, n - 1)
    return narcissistic_traits[random_index]


def randget_avoid_trait() -> str:
    n = len(avoidant_traits)
    random_index = random.randint(0, n - 1)
    return avoidant_traits[random_index]

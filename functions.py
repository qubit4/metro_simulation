import statistics
import random
from classes_sim import Passenger
from objects import lineA, lineB, lineC


def average_wait_time(wait_times):

    average_wait = round(statistics.mean(wait_times))
    print("Average waiting time is {} minutes".format(average_wait))


def average_travel_time(travel_times):

    average_travel = round(statistics.mean(travel_times))
    print("Average travel time is {} minutes".format(average_travel))


def total_carried(train1, train2):

    print("Train 1 carried {} passengers in total".format(train1.carried))
    print("Train 2 carried {} passengers in total".format(train2.carried))


def user_input():
    while True:
        try:
            passenger_count = int(
                input("Number of passengers (starting journey in regular intervals): "))

            interval = int(input("Regular interval (in minutes): "))

            choice = int(input(
                "Prague Metro -- Press 1 for Line A, Press 2 for Line B, press 3 for Line C: "))

            chosen_line = lineA if choice == 1 else lineB if choice == 2 else lineC

            duration_sim = int(input("Duration of simulation (in minutes): "))

            return passenger_count, interval, chosen_line, duration_sim

        except ValueError:
            print("Not a valid input")


def run_metro(env, passenger_count, interval, chosen_line, train1, train2):

    cycle = 0

    while True:
        # generating passengers number 1, 2, 3... interval... passengers 4, 5, 6... interval...
        for passenger in range((1 + (passenger_count * cycle)), (passenger_count + 1) + (passenger_count * cycle)):
            # some passengers travelling in one direction, others in another direction
            line = random.choice([chosen_line, list(reversed(chosen_line))])
            direction = "forth" if line == chosen_line else "back"
            passenger = Passenger(env, passenger, line, direction)
            # ensuring passengers are taking the train going in the correct direction
            right_train = passenger.choose_train(train1, train2)
            # main process
            env.process(passenger.travel(env, right_train))

        cycle += 1
        # the same process will happen with new passengers after chosen interval
        yield env.timeout(interval)

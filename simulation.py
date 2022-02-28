import simpy

from classes_sim import Train, wait_times, travel_times
from functions import average_wait_time, average_travel_time, total_carried, user_input, run_metro


def main():

    # intro and input
    print("Metro Simulation \n")
    passenger_count, interval, chosen_line, duration_sim = user_input()
    print("\nSimulation step-by-step: \n")

    # initializing objects
    env = simpy.Environment()
    train1 = Train(env, "1", chosen_line[0], "forth", timestamp=0, carried=0)
    train2 = Train(env, "2", chosen_line[-1], "back", timestamp=0, carried=0)

    # two trains running in opposite directions
    env.process(train1.move(env, chosen_line))
    env.process(train2.move(env, list(reversed(chosen_line))))

    # main process
    env.process(run_metro(env, passenger_count, interval, chosen_line,
                train1, train2))
    env.run(until=duration_sim)

    # statistics
    print("\nStatistics: \n")
    average_wait_time(wait_times)
    average_travel_time(travel_times)
    total_carried(train1, train2)


if __name__ == "__main__":
    main()

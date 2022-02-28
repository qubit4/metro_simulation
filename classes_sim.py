import simpy
import random


class Train:
    def __init__(self, env, number, position, direction, timestamp, carried):
        self.env = env
        self.number = number
        self.position = position
        self.direction = direction
        self.timestamp = timestamp
        self.carried = carried

    def move(self, env, line):

        yield env.timeout(self.timestamp)

        # reverse_var serves to periodically reverse train's direction and route
        reverse_var = True
        while True:
            for i in range(len(line)):
                temp = line if reverse_var else list(reversed(line))

                self.position = temp[i]
                self.timestamp = env.now
                print("Train number {} arriving at {} at time {}".format(
                    self.number, self.position, self.timestamp))
                # interval between stations: 2 minutes
                yield self.env.timeout(2)

            reverse_var = not reverse_var
            self.direction == "forth" if self.direction == "back" else "back"


# lists for statistics
wait_times = []
travel_times = []


class Passenger:
    def __init__(self, env, number, line, direction):
        self.env = env
        self.number = number
        self.line = line
        self.direction = direction
        self.start = random.choice(line[:-1])
        self.destination = random.choice(line[line.index(self.start)+1:])

    def choose_train(self, train1, train2):
        right_train = train1 if train1.direction == self.direction else train2
        return right_train

    def travel(self, env, train):

        start_wait = env.now
        travelling = False

        print("Passenger {} starting journey at {} at time {} and travelling to destination {}".format(
            self.number, self.start, start_wait, self.destination))

        while True:

            if self.start == train.position:
                print("Passenger {} boarding train {} at {} at time {}".format(
                    self.number, train.number, self.start, train.timestamp))

                end_wait = env.now
                wait_time = end_wait - start_wait
                wait_times.append(wait_time)

                start_travel = env.now
                travelling = True

            yield self.env.timeout(2)

            if self.destination == train.position and travelling == True:
                print("Passenger {} leaving train {} at {} at time {}".format(
                    self.number, train.number, self.destination, env.now))

                end_travel = env.now
                travel_time = end_travel - start_travel
                travel_times.append(travel_time)

                print("Passenger {} waited {} minutes at {} and travelled on train {} for {} minutes".format(
                    self.number, wait_time, self.start, train.number, travel_time))

                train.carried += 1

                break

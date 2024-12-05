import sys
import utils
import day01, day02, day03, day04

def runDay(day):
    print(f"###########DAY {day}###########")
    match day:
        case "1":
            print("###########STAR 1###########\n")
            print("Solving Star 1 Nieve approach:", day01.SolveStar1()) # faster using heap 2 come
            utils.time_it("Star 1 Solution", day01.SolveStar1)

            print("###########STAR 2###########\n")
            print("Solving Star 2:", day01.SolveStar2())
            utils.time_it("Star 2 Solution", day01.SolveStar2)

        case "2":
            print("###########STAR 1###########\n")
            print("Solving Star 1:", day02.SolveStar1())
            utils.time_it("Star 1 Solution", day02.SolveStar1)

            print("###########STAR 2###########\n")
            print("Solving Star 2:", day02.SolveStar2())
            utils.time_it("Star 2 Solution", day02.SolveStar2)
        case "3":
            print("###########STAR 1###########\n")
            print("Solving Star 1:", day03.SolveStar1())
            utils.time_it("Star 1 Solution", day03.SolveStar1)

            print("###########STAR 2###########\n")
            print("Solving Star 2:", day03.SolveStar2())
            utils.time_it("Star 2 Solution", day03.SolveStar2)

        case "4":
            print("###########STAR 1###########\n")
            print("Solving Star 1:", day04.SolveStar1())
            utils.time_it("Star 1 Solution", day04.SolveStar1)

            print("###########STAR 2###########\n")
            print("Solving Star 2:", day04.SolveStar2())
            utils.time_it("Star 2 Solution", day04.SolveStar2)
        case _:
            print("Invalid day:", day)


def runAllDays():
    days = ["1", "2", "3", "4"]

    for day in days: 
        runDay(day)


if __name__ == '__main__':
    if len(sys.argv) > 1:
		# Run a specific day
        day = sys.argv[1]
        runDay(day)
    else:
	    # Run all days if no argument is passed
        runAllDays()
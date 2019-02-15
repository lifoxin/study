import requests

res = requests.get("https://github.com/timeline.json")

def test1(test4):
    print("----1----")
    def test_in():
        print("---2---")
        return test4()
    return test_in

def test2(test4):
    print("----3----")
    def test_in():
        print("---4---")
        return test4()
    return test_in

@test1
@test2
def test3():
    print("-----5-----")

test3()
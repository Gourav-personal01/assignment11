#python code to create a process using the multiprocessing module.

import multiprocessing
def test():
    print("This is my multiprocessing program")

if __name__ == "__main__":
    m = multiprocessing.Process(target=test)
    print("this is my main prog")
    m.start()
    m.join()
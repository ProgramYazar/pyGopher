#!/usr/bin/env python
# coding: utf-8

# written by İlter Engin KIZILGÜN programyazar@gmail.com

from threading import Thread, Lock
from Queue import Queue
import time

class WaitGroup(object):

	def __init__(self):
		self.wg = Queue()

	def add(self, workNumber):
		for i in range(workNumber):
			self.wg.put(1)

	def done(self):
		self.wg.get()

	def wait(self):
		while self.wg.qsize() > 0:
			time.sleep(0.01)


class Chan(Queue):
	def __init__(self, N=1):
		Queue.__init__(self, maxsize=N)

	def send(self, item):
		self.put(item)

	def get(self):
		return self.get()




def go(func, *args):
	t = Thread(target=func, args=args)
	t.setDaemon(True)
	t.start()



# --------------------- TEST ---------------------

import random

def test_print(i, wg):
	sleep_time = random.randrange(1, 1000) * 1.0 / 1000.0
	time.sleep(sleep_time)
	print i
	wg.done()

def test():
	wg = WaitGroup()
	ch = Chan()
	for i in range(10):
		wg.add(1)
		go(test_print, i, wg )

	wg.wait()

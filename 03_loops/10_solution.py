#10. Exponential Backoff
#Problem: Implement an exponential backoff strategy that doubles the wait time between retries,
# starting from 1 second, but stops after 5 retries.


from time import time
import time
wait_time = 1
max_retries = 5
retries = 0

while retries < max_retries:
  print("Attempting operation...",retries + 1,"- Wait time:" ,wait_time,"seconds")
  time.sleep(wait_time)
  wait_time *=2
  retries += 1
from core.queue_lock import QueueLock

lock = QueueLock()

print("\n=== FIRST ACQUIRE ===\n")
print(lock.acquire())

print("\n=== SECOND ACQUIRE ===\n")
print(lock.acquire())

print("\n=== LOCKED ===\n")
print(lock.is_locked())

lock.release()

print("\n=== AFTER RELEASE ===\n")
print(lock.is_locked())

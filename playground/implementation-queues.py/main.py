from mail import Mail

class Queue:
  """Class Queue. Base class"""
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def enqueue(self, from_email, to, body, subject):
    """Enqueue method to add a element to the end of the queue"""
    new_mail = Mail(from_email, to, body, subject)
    if self.is_empty():
      self.first = new_mail
    else:
      self.last.next = new_mail
    self.last = new_mail
    self.length += 1

  def dequeue(self):
    """Dequeue method to delete the first element of the queue"""
    if self.is_empty():
      raise IndexError("La cola está vacía")
    removed_mail = self.first
    if self.length == 1:
      self.first = None
      self.last = None
    else:
      self.first = removed_mail.next
    removed_mail.next = None
    self.length -= 1
    return removed_mail

  def peek(self):
    """Peek method"""
    if self.is_empty():
      raise IndexError("La cola está vacía")
    return self.first

  def is_empty(self):
    """Is empty method"""
    return self.length == 0

  def size(self):
    """Size method"""
    return self.length
  
queue = Queue()
  
queue.enqueue(
  "user1@example.com",
  "support@example.com",
  "Body 1",
  "Subject 1"
)

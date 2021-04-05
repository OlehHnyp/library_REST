from django.db import models, DataError, IntegrityError

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
import datetime


class Order(models.Model):

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user", default="")
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="book", default="")
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(null=True)
    plated_end_at = models.DateTimeField(null=True)

    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        id = f"'id': {self.id}, "
        user = f"'user': {repr(self.user)}, "
        book = f"'book': {repr(self.book)}, "
        created_at = f"'created_at': '{(self.created_at)}', "
        end_at = f"'end_at': '{self.end_at}', "
        plated_end_at = f"'plated_end_at': '{self.plated_end_at}'"

        if self.end_at is None:
            end_at = "'end_at': None, "
        return id+user+book+created_at+end_at+plated_end_at

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'

    def to_dict(self):
        d = {
            'id': self.id,
            'user': self.user,
            'book': self.book,

            'created_at': int(self.created_at.timestamp()),
            'end_at': int(self.end_at.timestamp()),
            'plaetd_end_at': int(self.plated_end_at.timestamp()),
        }
        return d

    @ staticmethod
    def create(user, book, plated_end_at):
        if book.count > 1:
            try:
                order = Order(user=user, book=book,
                              plated_end_at=plated_end_at)
                order.save()
                return order
            except ValueError:
                pass

    @ staticmethod
    def get_by_id(order_id):
        try:
            return Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            pass

    def update(self, plated_end_at=None, end_at=None):

        if plated_end_at:
            self.plated_end_at = plated_end_at
        if end_at:
            self.end_at = end_at

        self.save()

    @ staticmethod
    def get_all():
        return list(Order.objects.all())

    @ staticmethod
    def get_not_returned_books():
        return list(Order.objects.filter(end_at=None))

    @ staticmethod
    def delete_by_id(order_id):
        try:
            Order.objects.get(id=order_id).delete()
            return True
        except Order.DoesNotExist:
            return False

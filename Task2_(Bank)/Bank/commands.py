from decimal import Decimal, InvalidOperation
from math import trunc
from django.db.transaction import atomic
from Bank.models import Client


@atomic
def deposit(name: str = None, amount: str = None, *_, **__) -> str:
    if name is None:
        return "Missing the 'name' argument"
    if amount is None:
        return "Missing the 'amount' argument"
    try:
        amount = Decimal(amount)
    except InvalidOperation:
        return 'Invalid argument of amount'
    client, is_new_client = Client.objects.get_or_create(name=name)
    client.balance += amount
    client.save()
    if is_new_client:
        return f"{client.name} was added; {client.name}'s balance: {client.balance}"
    else:
        return f"{client.name}'s balance was updated; {client.name}'s balance: {client.balance}"


@atomic
def withdraw(name: str = None, amount: str = None, *_, **__) -> str:
    if name is None:
        return "Missing the 'name' argument"
    if amount is None:
        return "Missing the 'amount' argument"
    try:
        amount = Decimal(amount)
    except InvalidOperation:
        return 'Invalid argument of amount'
    client, is_new_client = Client.objects.get_or_create(name=name)
    client.balance -= amount
    client.save()
    if is_new_client:
        return f"{client.name} was added; {client.name}'s balance: {client.balance}"
    else:
        return f"{client.name}'s balance was updated; {client.name}'s balance: {client.balance}"


@atomic
def balance(name: str = None, *_, **__) -> str:
    if name is None:
        return '\n'.join(map(lambda cli: cli.human_view, Client.objects.all()))
    else:
        try:
            return str(Client.objects.get(name=name).human_view)
        except Client.DoesNotExist:
            return 'NO CLIENT'


@atomic
def transfer(sender_name: str = None, recipient_name: str = None, amount: str = None, *_, **__) -> str:
    if sender_name is None:
        return "Missing the 'sender_name' argument"
    if recipient_name is None:
        return "Missing the 'recipient_name' argument"
    if amount is None:
        return "Missing the 'amount' argument"
    try:
        amount = Decimal(amount)
    except InvalidOperation:
        return 'Invalid argument of amount'
    if amount < 0:
        return 'Amount is negative'
    elif amount == 0:
        return f'{sender_name} --({amount})--> {recipient_name}'
    else:
        try:
            sender = Client.objects.get(name=sender_name)
            if sender.balance > amount:
                recipient, is_new_client = Client.objects.get_or_create(name=recipient_name)
                sender.balance -= amount
                recipient.balance += amount
                sender.save()
                recipient.save()
                if is_new_client:
                    return f'{sender_name} --({amount})--> {recipient_name} [New client]'
                else:
                    return f'{sender_name} --({amount})--> {recipient_name}'
            else:
                return f"{sender_name} doesn't have enough money for the transfer!"
        except Client.DoesNotExist:
            return f"{sender_name}'s account does not exist"


@atomic
def income(percent: str = None, *_, **__) -> str:
    if percent is None:
        return "Missing the 'percent' argument"
    try:
        percent = Decimal(percent)
    except InvalidOperation:
        return 'Invalid argument of percent'
    clients = Client.objects.filter(balance__gte=0)
    for client in clients:
        client.balance = Decimal(trunc(client.balance + (client.balance / 100 * percent)))
        client.save()
    return f'Balance updated for {clients.count()} clients'

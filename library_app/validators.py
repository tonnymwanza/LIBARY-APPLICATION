from django.core.signing import Signer

signer = Signer()
value = signer.sign('this is my first signature to make')
print(value)
# coding=utf-8

from unittest.case import TestCase
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey
from ellipticcurve.signature import Signature
from ellipticcurve.utils.file import File


class OpensslTest(TestCase):

    def testAssign(self):
        # Generated by: openssl ecparam -name secp256k1 -genkey -out privateKey.pem
        privateKeyPem = File.read("test/privateKey.pem")

        privateKey = PrivateKey.fromPem(privateKeyPem)

        message = File.read("test/message.txt")

        signature = Ecdsa.sign(message=message, privateKey=privateKey)

        publicKey = privateKey.publicKey()

        self.assertTrue(Ecdsa.verify(message=message, signature=signature, publicKey=publicKey))

    def testVerifySignature(self):
        # openssl ec -in privateKey.pem -pubout -out publicKey.pem

        publicKeyPem = File.read("test/publicKey.pem")

        # openssl dgst -sha256 -sign privateKey.pem -out signature.binary message.txt
        signatureDer = File.read("test/signatureDer.txt", "rb")

        message = File.read("test/message.txt")

        publicKey = PublicKey.fromPem(publicKeyPem)

        signature = Signature.fromDer(string=signatureDer)

        self.assertTrue(Ecdsa.verify(message=message, signature=signature, publicKey=publicKey))

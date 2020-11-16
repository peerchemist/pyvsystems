VSYS = 100000000
DEFAULT_TX_FEE = int(0.1 * VSYS)
DEFAULT_FEE_SCALE = 100
DEFAULT_SUPER_NODE_NUM = 15

DEFAULT_PAYMENT_FEE = DEFAULT_TX_FEE
DEFAULT_LEASE_FEE = DEFAULT_TX_FEE
DEFAULT_CANCEL_LEASE_FEE = DEFAULT_TX_FEE
DEFAULT_REGISTER_CONTRACT_FEE = 100*VSYS
DEFAULT_EXECUTE_CONTRACT_FEE = int(0.3*VSYS)
DEFAULT_CONTEND_SLOT_FEE = 50000 * VSYS
DEFAULT_RELEASE_SLOT_FEE = DEFAULT_TX_FEE
DEFAULT_DBPUT_FEE = 1 * VSYS

MAX_ATTACHMENT_SIZE = 140
MAX_DB_KEY_SIZE = 30
MIN_DB_KEY_SIZE = 1
MAX_NONCE = 4294967295
MAX_TX_HISTORY_LIMIT = 10000
MIN_CONTEND_SLOT_BALANCE = 1000000 * VSYS
MIN_CONTRACT_BYTE_SIZE = 8

THROW_EXCEPTION_ON_ERROR = True
CHECK_FEE_SCALE = True

DEFAULT_CHAIN = 'mainnet'
DEFAULT_CHAIN_ID = 'M'

TESTNET_CHAIN = 'testnet'
TESTNET_CHAIN_ID = 'T'

DEFAULT_TESTNET_NODE = 'http://test.v.systems:9922'
DEFAULT_TESTNET_API_KEY = ''


DEFAULT_NODE = 'http://127.0.0.1:9922'
DEFAULT_API_KEY = ''

ADDRESS_VERSION = 5
ADDRESS_CHECKSUM_LENGTH = 4
ADDRESS_HASH_LENGTH = 20
ADDRESS_LENGTH = 1 + 1 + ADDRESS_CHECKSUM_LENGTH + ADDRESS_HASH_LENGTH

PAYMENT_TX_TYPE = 2
LEASE_TX_TYPE = 3
LEASE_CANCEL_TX_TYPE = 4
CONTEND_SLOT_TX_TYPE = 6
RELEASE_SLOT_TX_TYPE = 7
REGISTER_CONTRACT_TX_TYPE = 8
EXECUTE_CONTRACT_FUNCTION_TX_TYPE = 9
DBPUT_TX_TYPE = 10

LEASE_TX_ID_BYTES = 32

Contract_Token_Without_Split = "3GQnJtxDQc3zFuUwXKbrev1TL7VGxk5XNZ7kUveKK6BsneC1zTSTRjgBTdDrksHtVMv6nwy9Wy6MHRgydAJgEegDmL4yx7tdNjdnU38b8FrCzFhA1aRNxhEC3ez7JCi3a5dgVPr93hS96XmSDnHYvyiCuL6dggahs2hKXjdz4SGgyiUUP4246xnELkjhuCF4KqRncUDcZyWQA8UrfNCNSt9MRKTj89sKsV1hbcGaTcX2qqqSU841HyokLcoQSgmaP3uBBMdgSYVtovPLEFmpXFMoHWXAxQZDaEtZcHPkrhJyG6CdTgkNLUQKWtQdYzjxCc9AsUGMJvWrxWMi6RQpcqYk3aszbEyAh4r4fcszHHAJg64ovDgMNUDnWQWJerm5CjvN76J2MVN6FqQkS9YrM3FoHFTj1weiRbtuTc3mCR4iMcu2eoxcGYRmUHxKiRoZcWnWMX2mzDw31SbvHqqRbF3t44kouJznTyJM6z1ruiyQW6LfFZuV6VxsKLX3KQ46SxNsaJoUpvaXmVj2hULoGKHpwPrTVzVpzKvYQJmz19vXeZiqQ2J3tVcSFH17ahSzwRkXYJ5HP655FHqTr6Vvt8pBt8N5vixJdYtfx7igfKX4aViHgWkreAqBK3trH4VGJ36e28RJP8Xrt6NYG2icsHsoERqHik7GdjPAmXpnffDL6P7NBfyKWtp9g9C289TDGUykS8CNiW9L4sbUabdrqsdkdPRjJHzzrb2gKTf2vB56rZmreTUbJ53KsvpZht5bixZ59VbCNZaHfZyprvzzhyTAudAmhp8Nrks7SV1wTySZdmfLyw7vsNmTEi3hmuPmYqExp4PoLPUwT4TYt2doYUX1ds3CesnRSjFqMhXnLmTgYXsAXvvT2E6PWTY5nPCycQv5pozvQuw1onFtGwY9n5s2VFjxS9W6FkCiqyyZAhCXP5o44wkmD5SVqyqoL5HmgNc8SJL7uMMMDDwecy7Sh9vvt3RXirH7F7bpUv3VsaepVGCHLfDp9GMG59ZiWK9Rmzf66e8Tw4unphu7gFNZuqeBk2YjCBj3i4eXbJvBEgCRB51FATRQY9JUzdMv9Mbkaq4DW69AgdqbES8aHeoax1UDDBi3raM8WpP2cKVEqoeeCGYM2vfN6zBAh7Tu3M4NcNFJmkNtd8Mpc2Md1kxRsusVzHiYxnsZjo "

Contract_Token_With_Split = "3dPGAWbTw4srh5hmMiRUhHtcxmXXLUooKGAfnmz11j5NruyJpBzZpgvADMdZS7Mevy5MAHqFbfHYdfqaAe1JEpLWt1pJWLHZBV62zUhLGmVLXUP5UDvSs24jsBRHqZMC71ciE1uYtgydKxCoFJ3rAgsYqp7GDeTU2PXS5ygDmL6WXmbAYPS8jE4sfNUbJVwpvL1cTw4nnjnJvmLET8VmQybxFt415RemV3MFPeYZay5i5gMmyZa63bjzK1uMZAVWA9TpF5YQ1NTZjPaRPvQGYVY4kY9L4LFJvUG2bib1QaNh7wUAQnTzJfRYJoy1aegFGFZFnBGp9GugH4fHAY69vGmZQnhDw3jU45G9odFyXo3T5Ww4R5szegbjCUKdUGpXf9vY2cKEMJ7i8eCkFVG1dDFZeVov1KMjkVNV8rDBDYfcp3oSGNWQQvGSUT5iGUvDRN8phy1UpR3A9uMVebvjLnVzPx9RyqQ8HaXLM8vPhLuWLoh5hk1Zi1n9nwz55XvKDYjP6eeB55yK5vpg8xjaYDnw9bjYV7ZmS7LAsHvXfnwi8y2W6vk2hGvs4rtR1vNRZSQMPGRRSuwCRJL1yngH6uHWwm2ajWxc684jApuoLdyjZomfCtdpabSyU3kp9Lrn8zT8BVY332sJPQU6gTQi8ke9s9dBxCae4cfSQM6HhuBmFc5KKWHCVG4bm4KZRYbMtidw8ZZnjaAMtcGq7k3Se6GXaTxdS3GcuttB3VB7njypyzuqAcfCdYb9ht8Y1WuTCZ1aLsXsL6eydfk2WLJVrqYpbTk6AchV5gMAEopvc3qXvzrDCedjtNsDmA56Lh6PxrrKr8aV8Wzz8aMaQ88YsVBpE8J4cDkxzo31AojhzEGVBKLmpb3bjmsaw9VkpB6yL8ngYs8eJMSPdM289TSMaEmG4eHt1jezpHTKxkuB9cwqcvhGNLWuv8KXQkik5pRMXV67Qs2FvjpzeJ81z2hnVh1wCtsa6M6qAG1gsqLHa1AVMRzsowafC99uDexwWMBS2RqsZWZBXJcUiNVULjApSnoBREYfHYEpjJ152hnTYZCAwpZMWEkVdBQpZ3zk8gbfLxB4fWMfKgJJucbKPGp1K56u7P8MHQu9aNb9dEof2mwX8rTHjk8jSQ7kXVX4Mf1JqMRWWftkV3GmU1nqYhxRGu4FjDNAomwTr5epHpcMF6P5oiXcLWh5BFQVmGYKz129oizAyUJBsZdxr2WZEGDieLxUg8cve25g28oTuCVENST4z1ZsFAN9wTa1"

Contract_Lock = "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"

Contract_Payment_Channel = "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"

Contract_Atomic_Swap = "4CrYZXauEHTHvUcNbU2qxvYSgdxPkSBum4PAUfytuZu7Nn56L59op72uKJUBMnF8dk8dLb5k63M9236s8S2yH4FTeWFP4zjfpkx9HGwjAuh6n6WJyxWE1S5HHH2cQLy4xk5B4iMpQKyHQwrQDn3zWwQQPsrfnwaHX1F3V2zKHKx15QYATS784BGfz9NeY72Ntdz2Cgsf6MLQE1YKdgdRfpryCwadqs5xchALCPYLNg6ECSxzPDa4XdS8ywTWzRpiajTGZA1z9YoQZiUMYBwM8S2G4ttZJkgrWTqpXuxberLv3CWZm7kp8bwvg577p8kJ7zAugTgaBU9vzSRFzi3fWtGEP1TPuMCjLSQfskepjoA73UmptqjHPGBtfDxXQmDqB6Gdgin3T7Et4feVDhQjbJJCq9FJVpHsiV9zXyCiZ6DTj2tjx2uUjS8PvVERfjvhPKt8vXctBq64F3s5X3jVX88A1FKRAiiJgH2FoM9cMxAgpLqJxeDQeHwj5CqgCjTXX6mF3JXrJRfjejoAY4LhPcWc79dgKUMFVw5uPESMmHm7p3rVEE5su4n6gmKiaA4L1EVd4spbqWzU3NrvW985kLpBMdcpknqqWCUrHE2buf3h1bzSxCSCV6zmn8Qi4cwJcG5t2yo3ZqcfzDB88xTDAZGqr5MGk6Zves25wvbJgHgrD9xA9qSmHXeSYMv4FkAjzmLFWMiDKGDQ62rSWDMykDLim6p3LVSCqLBXa7f7h7bTUYFZ8fNQBACyWwdagKBqiy8BgejSVquekQ7Rwf5EE5ZqegQZtUEwQCGDowFv2ZUcjReH8wo3QXTPtR5EnQDLpbiAuCkMokgZeeEWgRAL9B6G8vQn8YAmEq9JcvVYoWAikgmK7yEF9m5PMpmFpZ8SAncrej4cUmt2GeB5j43J9hLgyhboE6i1wg4BS4p98JFTgp76SuQEXcnd811wMLiLko24qcpRD1UAbKcB6eqpJL2g53nVXScntY8STp5sTve4tsLiBY6PWKYd3AzRWxgXEFLeei8ocnzxJdEFX6TuXApf8n4jBVzdRwziduipTK5AJDzqVviagoCYS7LTvoXT5yhk9fF7NpK7bQykFh9Gj1qk4Rnh5MKV9FjqrVDSPE7Bswz69oGJVg3duutWrqVWgU1BhUSYxLakGcKnf6d5LQk9ctBpM96kSdhQyFsgCnUrfSczihmiLsjYE2rxnxXMx38kHGhSqFD1TSGtBfxQNUjednBeJ9uELyT3HBRn9RCu9MmC2fKZNWNk7vaHJais8Pgg5jB2mTkDH9c1DLTvRa8BF8Jz7Ekqmfqb5Q4CTL39veS2Fa54VYMzN5TeHPysKJtS96E2fkQ4XnXwzoXJ53k1Sm7FFgLuqw76jfVkbS3YbjWHQLF9BVkYkcx7Um6sHQarJ4xvNq2GR9RtoWXxbmBNuXtHFni8PM9WzEtJHsiTHh84AAQ6V6FQRiEkTMheSaDoj5EhvDASH2bMT9QXpdNQMjXa95rtnkdPyzzAXr5TNUEbEuB98H47DyBbqfp66ZRWgnXfeJpHgBs4aQnwmnSt3MhH9fYoZBwhbp5kxRfcTbWbogdtoX2KnkJzrR2c8cnK2iiarSDY"

class ContractMeta:
    token_address_version = -124
    check_sum_length = 4

    language_code_byte_length = 4
    language_version_byte_length = 4

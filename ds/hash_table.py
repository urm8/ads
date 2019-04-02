

class HashTable:
    """
    Simple hash map implementation jff
    """
    def __init__(self, size=16):
        self._keys = [None for _ in range(size)]
        self._values = [None for _ in range(size)]
        self._size = size
        self._load = 0

    def _hash(self, key):
        return hash(key) % self._size

    def _rehash(self):
        old_size = self._size
        self._size = int(self._size * 1.5)
        n_k = [None, ] * self._size
        n_v = [None, ] * self._size
        for k, v in zip(self._keys, self._values):
            ih = h = self._hash(k)
            while not n_k[h] is None:
                h = self._hash(h)
                if ih == h:
                    return self._rehash()
            n_k[h], n_v[h] = k, v
        self._keys, self._values = n_k, n_v

    def __setitem__(self, key, value):
        initial_hash = hash_ = self._hash(key)
        while self._keys[hash_] not in (key, None):
            hash_ = self._hash(hash_)
            if initial_hash == hash_:
                self._rehash()
        if self._keys[hash_] is None:
            self._keys[hash_], self._values[hash_] = key, value
            self._load += 1
        else:
            old_val, self._values[hash_] = self._values[hash_], value
            return old_val

        if 1.0 * self._load / self._size > 0.7:
            self._rehash()

    def __getitem__(self, key):
        if self._keys[self._hash(key)] != key:
            raise KeyError('no such key %s' % key)
        return self._values[self._hash(key)]

    def __delitem__(self, key):
        hash_ = self._hash(key)
        self._keys.pop(hash_)
        self._values.pop(hash_)

    def __contains__(self, key):
        return self._keys[self._hash(key)] == key

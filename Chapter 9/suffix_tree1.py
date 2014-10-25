# coding: shift_jis
#
# sufftree.py : 接尾辞木 (Suffix Tree)
#               (Generalized suffix tree)
#
#               Copyright (C) 2009 Makoto Hiroi
#

# 定数
ROOT = -1
MAX_LEN = 0x7fffffff


# 基本クラスの定義
class BaseNode:
  def __init__(self, start, depth):
        self.start = start      # 開始位置
        self.depth = depth      # 接頭辞の長さ (木の深さ)

# 葉の定義
class Leaf(BaseNode):
    def __init__(self, start, depth, id):
        BaseNode.__init__(self, start, depth)
        self.id = id

    # 節の長さ
    def len(self): return MAX_LEN

    # 葉の巡回
    def traverse_leaf(self): yield self

# 節の定義
class Node(BaseNode):
    # 初期化
    def __init__(self, start, depth):
        BaseNode.__init__(self, start, depth)
        self.child = None       # 子のリンク
        self.bros = None        # 兄弟のリンク
        self.link = None        # サフィックスリンク

    # 子を探す
    def search_child(self, buff, size, x):
        child = self.child
        while child is not None:
            if child.start < size and buff[child.start] == x:
                return child
            child = child.bros
        return None

    # 子を挿入する
    def insert_child(self, child):
        child.bros = self.child
        self.child = child

    # 子を削除する
    def delete_child(self, child):
        if self.child is child:
            self.child = child.bros
        else:
            # リンクをたどる
            node = self.child
            while node.bros is not None:
                if node.bros is child:
                    node.bros = node.bros.bros
                    break
                node = node.bros

    # 節の長さを求める
    def len(self):
        if self.start == ROOT: return 0
        return self.child.depth - self.depth

    # 葉を巡回する
    def traverse_leaf(self):
        node = self.child
        while node is not None:
            for x in node.traverse_leaf():
                yield x
            node = node.bros

# Suffix Tree
class SuffixTreeError(Exception): pass

class SuffixTree:
    def __init__(self, buff):
        self.buff = buff
        self.size = len(self.buff)
        self.root = Node(ROOT, 0)
        self.root.link = self.root
        self.sets = 0
        self.interval = [0]
        #
        self.make_suffix_tree(0)
        self.sets += 1

    # 接尾辞木に文字列を追加する
    def add(self, buff):
        self.buff += buff
        n = self.size
        self.interval.append(n)
        self.size = len(self.buff)
        self.make_suffix_tree(n)
        self.sets += 1

    def make_suffix_tree(self, bi):
        # bi は buff の位置
        ni = 0            # node 内の位置
        si = bi           # 照合開始位置
        node = self.root  # 照合中の節
        prev = node       # node の親節
        nlen = 0          # node の長さ
        while bi < self.size:
            if ni == nlen:
                # 次の子を探す
                child = node.search_child(self.buff, self.size, self.buff[bi])
                if child is None:
                    if si == bi:
                        # ルートに挿入
                        self.root.insert_child(Leaf(bi, 0, self.sets))
                        si += 1
                        bi += 1
                    else:
                        # 葉を挿入する
                        prev, node, nlen, ni, si, bi = self.insert_leaf(node, bi, si)
                else:
                    prev = node
                    node = child
                    nlen = child.len()
                    ni = 1
                    bi += 1
            else:
                if self.buff[bi] != self.buff[node.start + ni]:
                    # 節を分割して葉を挿入する
                    prev, node, nlen, ni, si, bi = self.divide_node(prev, node, ni, bi, si)
                else:
                    ni += 1
                    bi += 1
        #
        if si < bi:
            if nlen == ni:
                self.insert_leaf(node, bi, si)
            else:
                self.divide_node(prev, node, ni, bi, si)

    # サフィックスリンクをたどり葉を挿入していく
    def insert_leaf(self, node, bi, si):
        node.insert_child(Leaf(bi, node.depth + node.len(), self.sets))
        node = node.link
        si += 1
        while si < bi:
            if bi < self.size:
                child = node.search_child(self.buff, self.size, self.buff[bi])
                if child is not None:
                    return node, child, child.len(), 1, si, bi + 1
            node.insert_child(Leaf(bi, node.depth + node.len(), self.sets))
            node = node.link
            si += 1
        return self.root, self.root, 0, 0, si, bi


    # リンクをたどり節を分割して葉を挿入していく
    def divide_node(self, prev, node, ni, bi, si):
        link_node = self.insert_node(prev, node, bi, ni)
        si += 1
        while si < bi:
            prev, node, match = self.search_next_link(prev.link, si, bi)
            if match == 0:
                if bi < self.size:
                    child = node.search_child(self.buff, self.size, self.buff[bi])
                    if child is not None:
                        link_node.link = node
                        return node, child, child.len(), 1, si, bi + 1
                link_node.link = node
                return self.insert_leaf(node, bi, si)
            #
            link_node.link = self.insert_node(prev, node, bi, match)
            link_node = link_node.link
            si += 1
        #
        link_node.link = self.root
        return self.root, self.root, 0, 0, si, bi

    # 分割位置を求める
    def search_next_link(self, node, i, end):
        prev = node
        if node is not self.root:
            i += node.child.depth
        while i < end:
            child = node.search_child(self.buff, self.size, self.buff[i])
            j = child.len()
            if i + j > end:
                return node, child, end - i
            i += j
            prev = node
            node = child
        return prev, node, 0

    # データの挿入
    def insert_node(self, parent, node, match, sub_match):
        # node を new_node - node に分割する
        new_node = Node(node.start, node.depth)
        node.depth += sub_match
        node.start += sub_match
        # 子の付け替え
        parent.delete_child(node)
        parent.insert_child(new_node)
        new_node.insert_child(node)
        # new_node に葉を追加する
        new_node.insert_child(Leaf(match, node.depth, self.sets))
        return new_node

    #
    # アプリケーション
    #
    
    # 共通接頭辞の検索
    def search_pattern_sub(self, seq):
        size = len(seq)
        node = self.root
        i = 0
        while i < size:
            child = node.search_child(self.buff, self.size, seq[i])
            if child is None: return None
            j = 1
            k = child.len()
            while j < k:
                if i + j == size: return child
                if i + j == self.size or seq[i + j] != self.buff[child.start + j]:
                    return None
                j += 1
            i += j
            node = child
        return node

    def search_pattern(self, seq):
        node = self.search_pattern_sub(seq)
        if node is not None:
            for x in node.traverse_leaf():
                return True
        return False

    def search_pattern_all(self, seq):
        node = self.search_pattern_sub(seq)
        if node is None: return
        for x in node.traverse_leaf():
            yield x.id, x.start - x.depth - self.interval[x.id]

    # n 文字以上 m 回以上出現している文字列を求める
    def search_repeated_substring(self, node, n, m, a):
        if isinstance(node, Leaf):
            c = 1
            l = self.size - node.start
        else:
            # 葉の数を求める
            x = node.child
            c = 0
            while x is not None:
                c += self.search_repeated_substring(x, n, m, a)
                x = x.bros
            # 節の長さをチェック
            l = node.len()
        if l > 0 and c >= m:
            for k in xrange(l, 0, -1):
                if node.depth + k < n: break
                a.append((node.start - node.depth, node.start + k, c))
        return c

    def repeated_substring(self, n, m):
        a = []
        self.search_repeated_substring(self.root, n, m, a)
        return a

    # 2 回以上繰り返しのある最長の文字列を求める
    def search_longest_repeated_substring(self, node):
        if isinstance(node, Leaf):
            # 葉は該当しない
            return None
        else:
          max_node = node
          x = node.child
          while x is not None:
              y = self.search_longest_repeated_substring(x)
              if y is not None and max_node.child.depth < y.child.depth:
                  max_node = y
              x = x.bros
          return max_node

    def longest_repeated_substring(self):
        node = self.search_longest_repeated_substring(self.root)
        return node.start - node.depth, node.start + node.len()

    # id ごとにパターンが出現している回数を求める
    def count_pattern(self, seq):
        result = [0] * self.sets
        node = self.search_pattern_sub(seq)
        for x in node.traverse_leaf():
            result[x.id] += 1
        return result

    # n 文字以上で全ての id に出現している文字列を求める
    def search_common_substring(self, node, n, a):
        def add_cnt(src, dst):
            for x in xrange(self.sets): src[x] += dst[x]
        #
        if isinstance(node, Leaf):
            cnt = [0] * self.sets
            cnt[node.id] = 1
            return cnt
        else:
            x = node.child
            cnt = [0] * self.sets
            while x is not None:
                add_cnt(cnt, self.search_common_substring(x, n, a))
                x = x.bros
            # 節の長さをチェック
            l = node.len()
            if l > 0 and 0 not in cnt:
                for k in xrange(l, 0, -1):
                    if node.depth + k < n: break
                    a.append((self.buff[node.start - node.depth:node.start + k], cnt))
            return cnt

    def common_substring(self, n):
        a = []
        self.search_common_substring(self.root, n, a)
        return a

    # 全ての id で出現する最長の文字列を求める
    def search_longest_substring(self, node, a):
        if isinstance(node, Leaf):
            # 葉は該当しない
            return 1 << node.id
        else:
          x = node.child
          c = 0
          while x is not None:
              c |= self.search_longest_substring(x, a)
              x = x.bros
          if c == (1 << self.sets) - 1:
              if a[0].child.depth < node.child.depth:
                  a[0] = node
          return c

    def longest_common_substring(self):
        a = [self.root]
        self.search_longest_substring(self.root, a)
        return self.buff[a[0].start - a[0].depth:a[0].start + a[0].len()]

# デバッグ用表示ルーチン
def print_node(node, buff):
    if isinstance(node, Leaf):
        
        print '' * node.depth + buff[node.start:]
    else:
        if node.start == ROOT:
            print "root", id(node)
        else:
            print '' * node.depth + buff[node.start:node.start + node.len()]#, \
                  #id(node), id(node.link)
        x = node.child
        while x is not None:
            print_node(x, buff)
            x = x.bros

# 子の個数を数える
def count_child(node):
    a = 0
    x = node.child
    while x is not None:
        a += 1
        x = x.bros
    return a

# 同じ文字から始まる兄弟がないかチェックする
def check_same_child(node, buff):
    if isinstance(node, Node):
        x = buff[node.start]
        node = node.bros
        while node is not None:
            if node.start < len(buff) and buff[node.start] == x:
                raise SuffixTreeError, "error2"
            node = node.bros

# suffix link のチェック
def check_suffix_link(node, buff):
    len1 = node.len()
    len2 = node.link.len()
    depth1 = node.depth
    depth2 = node.link.depth
    if depth1 + len1 != depth2 + len2 + 1:
        raise SuffixTreeError, "suffix link error1"
    str1 = buff[node.start - depth1 + 1:node.start + len1] 
    str2 = buff[node.link.start - depth2:node.link.start + len2]
    if str1 != str2:
        raise SuffixTreeError, "suffix link error2"
    # print "OK", id(node), str1, str2

# suffix tree のチェック
def check_node(node, buff):
    if isinstance(node, Leaf):
        return 1
    else:
        # 節
        if node.start != ROOT:
            check_suffix_link(node, buff)
        if node.start != ROOT and count_child(node) < 2:
            raise SuffixTreeError, "error1"
        x = node.child
        a = 0
        while x is not None:
            check_same_child(x, buff)
            a += check_node(x, buff)
            x = x.bros
        return a

# 簡単なテスト
if __name__ == '__main__':
    st = SuffixTree("banana$")
    st.add("bananas&")
    print_node(st.root, st.buff)
    check_node(st.root, st.buff)
    for id, s in st.search_pattern_all("ana"):
        print id, s
    print st.count_pattern("ana")
    s, e = st.longest_repeated_substring()
    print st.buff[s:e]
    for s, e, c in st.repeated_substring(1, 2):
        print st.buff[s:e], c
    print "-----"
    st = SuffixTree("sandollar1")
    check_node(st.root, st.buff)
    print_node(st.root, st.buff)
    print "-----"
    for x in ["sandlot2", "handler3", "grand4", "pantry5"]:
        st.add(x)
        check_node(st.root, st.buff)
        print_node(st.root, st.buff)
        print st.common_substring(2)
        a = st.longest_common_substring()
        print a, 
        for x in st.search_pattern_all(a):
            print x,
        print
        print "-----"
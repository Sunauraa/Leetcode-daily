/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return node;
        
        unordered_map<Node*, Node*> m;
        unordered_set<Node*> visited;
        
        dfs(node, m, visited);
        
        // Optional: Print connections (similar to your Python code)
        for (auto& entry : m) {
            Node* original = entry.first;
            Node* clone = entry.second;
            for (Node* neighbor : original->neighbors) {
                cout << original->val << " " << neighbor->val << endl;
            }
        }
        
        return m[node];
    }
    
    void dfs(Node* n, unordered_map<Node*, Node*>& m, unordered_set<Node*>& visited) {
        if (visited.count(n)) return;
        
        visited.insert(n);
        
        if (!m.count(n)) {
            m[n] = new Node(n->val);
        }
        
        for (Node* neigh : n->neighbors) {
            if (!m.count(neigh)) {
                m[neigh] = new Node(neigh->val);
            }
            m[n]->neighbors.push_back(m[neigh]);
            dfs(neigh, m, visited);
        }
    }
};
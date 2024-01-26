class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& a) {
    //     vector<int>ans;
    //     vector<vector<int>>v(a.size()*2);
    //   //  cout<<v.size()<<" "<<v[0].size();
    //     for(int j=0;j<a.size();j++)
    //     {
    //         for(int i=0;i<a[j].size();i++)
    //         {
    //             v[i+j].push_back(a[i][j]);
    //         }
    //     }
    //     for(auto i:v)
    //     {
    //         for(auto j:i) ans.push_back(j);
    //     }  
    //     return ans;


    vector<int>ans;
    map<int,vector<int>>m;
    for(int i=0;i<a.size();i++)
    {
        for(int j=0;j<a[i].size();j++)
        {
            m[i+j].push_back(a[i][j]);
        }
    }
    for(auto i:m)
    {
        vector<int>v=i.second;
        reverse(v.begin(),v.end());
        for(auto j:v)
        {
            ans.push_back(j);
        }
    }
    return ans;
    }
};
#include <bits/stdc++.h>

using namespace std;

#define READ() 	    freopen("in.txt","r",stdin)
#define WRITE()     freopen("out.txt","w",stdout)
#define sf(n) 	    scanf("%d",&n)
#define sl(x)       scanf("%I64d",&x)
#define lsf(n) 	    scanf("%lld", &n)
#define pb(n) 	    push_back(n)
#define mem(x,y)    memset(x,y,sizeof(x))
#define D(x)      	cout << #x << " = " << x << endl
#define CHKRTE		assert(false)
#define YOLO        cout << "YOLO" << endl
#define NL			printf("\n")
#define EPS 	    1e-10
#define INF         INT_MAX
#define MAX         111
#define MOD         1000000007
#define LL          long long
#define endl        "\n"
#define pi          2.0*acos(0.0)
#define cnd         tree[idx]
#define lnd         tree[left]
#define rnd         tree[right]
#define callLeft    left,st,mid
#define callRight   right,mid+1,ed

LL modOfNegative(LL x,LL m) /// -x mod m
{
    LL xVal = ((llabs(x/m)+1)*m)*(-1) ;
    return llabs(x-xVal);
}

long long pow2(long long a, long long b, long long MOD2)
{
    long long x = 1, y = a;
    while (b > 0)
    {
        if (b % 2 == 1)
        {
            x = (x * y);
            if (x > MOD2)
                x %= MOD2;
        }
        y = (y * y);
        if (y > MOD2)
            y %= MOD2;
        b /= 2;
    }
    return x;
}

long long modInverse(long long a, long long m) /// (1/a)%m
{
    return pow2(a, m - 2, m);
}



/// hashing starts

/**
 given n strings.
 Q query : i,a,b and j,p,q
 tell if ith string [a...b] is equal to jth string [p...q]
**/

string sArr; /// working string that is used in hashing() function
string storeS[2]; /// stores n strings
LL storeHash[2];/// stores full hash of ith string string
LL storeLen[2];/// stores length of ith string string
vector <LL> vecHash[2];/// vecHash[i][j] stores hash of ith string, till position j
vector<string>substring[10000];
vector<LL>substringHashval[10000];
map<string,LL>substringMap;
vector<LL>unique_par;
map<string,LL>unique_par_map;
int mat[500][500];
/// hash1;
const LL base = 29;
const LL hashMod = 1009010791; /// prime dao!
/// hash1

/// precal modInv
LL modInvCal[MAX]; /// (1/(base^i))%hashmod
void genModInv()
{
    LL x = modInverse(base,hashMod);
    modInvCal[1] = x;
    modInvCal[0] = 1;
    for(int i=2;i<MAX;i++)
    {
        modInvCal[i] = (modInvCal[i-1] * x)%hashMod;
    }
}

/// precal pow
LL basePow[MAX];
void genPow()
{
    basePow[0] = 1;
    for(int i=1;i<MAX;i++)
    {
        basePow[i] = (basePow[i-1]*base)%hashMod;
    }
}

LL hashing(int len,string str1) /// hashing of ith string of length len
{
    LL hashVal = 0;
    for(int i=0;i<len;i++)
    {
        /// hash1
        LL x = str1[i] - 97 + 1;
        hashVal *= base; hashVal %= hashMod;
        hashVal += x; hashVal %= hashMod;

    }
    return hashVal;
}

LL getHashStartingAt(int iPos,LL mainHash,int len,int ithString)/// 0 to len-1
{
    if(iPos == 0)return mainHash;
    if(iPos == len)return 0;

    LL curHash = mainHash;
    curHash = curHash - (vecHash[ithString][iPos-1] * basePow[len-iPos])%hashMod;
    if(curHash < 0)curHash = modOfNegative(curHash,hashMod);
    else curHash %= hashMod;

    return curHash;
}

LL getHashOfSubString(int i,int j,LL mainHash,int len,int ithString) /// 0 to len-1
{
    LL curHash = getHashStartingAt(i,mainHash,len,ithString);
    curHash = curHash - getHashStartingAt(j+1,mainHash,len,ithString);
    if(curHash < 0)curHash = modOfNegative(curHash,hashMod);
    else curHash %= hashMod;

//    curHash = (curHash * modInverse(basePow[len-1-j],hashMod))%hashMod;
    curHash = (curHash * modInvCal[len-1-j])%hashMod;
    curHash %= hashMod;

    return curHash;
}

bool bruteSol(int i,int a,int b,int j,int p,int q)
{
    string s1 = "";
    for(int ii=a;ii<=b;ii++)s1 += storeS[i][ii];

    string s2 = "";
    for(int ii=p;ii<=q;ii++)s2 += storeS[j][ii];

//    cout << s1 << " " << s2 << endl;

    return (s1==s2);
}

/// hashing ends

bool solve(int i,int a,int b,int j,int p,int q)
{
    LL hashI = getHashOfSubString(a,b,storeHash[i],storeLen[i],i);
    LL hashJ = getHashOfSubString(p,q,storeHash[j],storeLen[j],j);
    return (hashI == hashJ);
}

int main()
{
    string str1;
    int i,j,c,c1=1,hashval,k=5,q=0;
    for(q=0;q<7;q++)
    {
        substringMap.clear();
        getline(cin,sArr);
    //storeS[i] = sArr;
        int len = sArr.size();


        i=0;
        //storeLen[i] = len;
        c=0;

        for(i=0;i<len;i++)
        {
            str1="";
            c=i;
            for(j=0;j<k;j++)
            {
                str1+=sArr[c];

                c++;
                if(c>=len)break;

            }
            if(str1.size()==k)
            substring[q].push_back(str1);
           // cout<<str1<<endl;
        }
        //substring[q].push_back(" mist");
        for(i=0;i<substring[q].size();i++)
        {
            str1= substring[q][i];
            hashval= hashing(str1.size(),str1);
            //ut<<str1<<" huhu "<<hashval<<" "<<substringMap[str1]<<endl;
            if(substringMap[str1]==0)
            {
                substringMap[str1]=hashval;
                substringHashval[q].push_back(hashval);
                //cout<<str1<<endl;

            }
            if(unique_par_map[str1]==0)
            {
                unique_par_map[str1]=hashval;
                unique_par.push_back(hashval);
            }


        }


    }
    for(i=0;i<unique_par.size();i++)
    {
        hashval= unique_par[i];
        for(j=0;j<7;j++)
        {
            for(q=0;q<substringHashval[j].size();q++)
            {
                if(substringHashval[j][q]==hashval)
                {
                    mat[i][j]=1;
                }
            }
        }
    }
    for(i=0;i<unique_par.size();i++)
    {
        for(j=0;j<7;j++)
        {
            cout<<mat[i][j]<<" ";
        }
        cout<<endl;
    }



    return 0;
}



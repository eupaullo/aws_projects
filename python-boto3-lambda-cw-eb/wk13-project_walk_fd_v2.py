#!/usr/bin/env python3.10
import os

# Date: 04/09/2023
# Name: Do Hyung Kim

# Title: create a script generating a list of dictionaries about files
# This is ver. 2 program

# Create an empty list and an empty dictionary
file_list=[]
dict_of_list={}

#def get_file_list(root, file_names, each_sub_dir):
#    print("This is the directory of ", os.path.join(root,each_sub_dir))
#    for each_file in file_names:
#        each_item = f"'path' : {os.path.join(root, each_sub_dir)}, 'size' : {os.stat(each_file).st_size}"
#        file_list.append(each_item)
#        print(each_item, sep="\n") # print each file item per line on computer screen
#    return file_list # return the created file_list list 

def get_tree_directory(dir='/home/dohyungkim2023/my-python-repo'):
    for root, sub_dir_names, file_names in os.walk(dir):
        #print (f"{root},\n{sub_dir_names}, {file_names}") # list sub directories and file names under the directory  
        if sub_dir_names ==[]:
#            each_file_list_per_each_dir = get_file_list(root, file_names, each_sub_dir='')
            print("This is the directory of ", os.path.join(root))
            for each_file in file_names:
                each_item = { 'path' : os.path.join(root, each_file), 'size' : os.path.getsize(os.path.join(root, each_file))}
                file_list.append(each_item)                 
                print(each_item, sep="\n")
        else:            
            for each_sub_dir in sub_dir_names: 
                for each_file in file_names:
                    each_item = { 'path' : os.path.join(root, each_file), 'size' : os.path.getsize(os.path.join(root, each_file))}
                    file_list.append(each_item)                 
                    print(each_item, sep="\n")
        
        
    print(file_list)






working_path = input("Enter the working directory pathway: ") # /home/dohyungkim2023/my-python-repo"
get_tree_directory(working_path)






'''
This script requires a manual entry of the directory pathway.
The above for loop with os.walk(dir) will walk through all the sub directories and all their files.
I initially thought that I should deal with sub_dir_names == [] case, as I concerned on reporting all sub directories
and there was a possibility that empty sub directories might be added to my list of files. 
Later, I realized that there was no reason to worry about that as we focused on files, 
as we are not usually interested in looking into any directories without a presence of a file in reality.

######################
~/my-python-repo/week13$ /bin/python3 /home/dohyungkim2023/my-python-repo/week13/wk13-project_walk_fd_v2.py
Enter the working directory pathway: /home/dohyungkim2023/my-python-repo
{'path': '/home/dohyungkim2023/my-python-repo/testing-functions.py', 'size': 4248}
{'path': '/home/dohyungkim2023/my-python-repo/string-info.py', 'size': 2679}
{'path': '/home/dohyungkim2023/my-python-repo/scopes.py', 'size': 2292}
{'path': '/home/dohyungkim2023/my-python-repo/.gitignore', 'size': 1799}
{'path': '/home/dohyungkim2023/my-python-repo/fizz-buzz.py', 'size': 1121}
{'path': '/home/dohyungkim2023/my-python-repo/py-if-elif-else.py', 'size': 1397}
{'path': '/home/dohyungkim2023/my-python-repo/using-dictionaries.py', 'size': 6584}
{'path': '/home/dohyungkim2023/my-python-repo/README.md', 'size': 152}
{'path': '/home/dohyungkim2023/my-python-repo/find_string.py', 'size': 1006}
{'path': '/home/dohyungkim2023/my-python-repo/split&join_again.py', 'size': 1930}
{'path': '/home/dohyungkim2023/my-python-repo/scope2.py', 'size': 1444}
{'path': '/home/dohyungkim2023/my-python-repo/fizz-buzz-item.py', 'size': 1203}
{'path': '/home/dohyungkim2023/my-python-repo/wk13-Mon-lesson-04032023.py', 'size': 6904}
{'path': '/home/dohyungkim2023/my-python-repo/using-list.py', 'size': 4017}
{'path': '/home/dohyungkim2023/my-python-repo/variations.py', 'size': 3297}
{'path': '/home/dohyungkim2023/my-python-repo/Hello_world.py', 'size': 53}
{'path': '/home/dohyungkim2023/my-python-repo/Hello_yourname.py', 'size': 1080}
{'path': '/home/dohyungkim2023/my-python-repo/using-generator.py', 'size': 2540}
{'path': '/home/dohyungkim2023/my-python-repo/testing-functions.py', 'size': 4248}
{'path': '/home/dohyungkim2023/my-python-repo/string-info.py', 'size': 2679}
{'path': '/home/dohyungkim2023/my-python-repo/scopes.py', 'size': 2292}
{'path': '/home/dohyungkim2023/my-python-repo/.gitignore', 'size': 1799}
{'path': '/home/dohyungkim2023/my-python-repo/fizz-buzz.py', 'size': 1121}
{'path': '/home/dohyungkim2023/my-python-repo/py-if-elif-else.py', 'size': 1397}
{'path': '/home/dohyungkim2023/my-python-repo/using-dictionaries.py', 'size': 6584}
{'path': '/home/dohyungkim2023/my-python-repo/README.md', 'size': 152}
{'path': '/home/dohyungkim2023/my-python-repo/find_string.py', 'size': 1006}
{'path': '/home/dohyungkim2023/my-python-repo/split&join_again.py', 'size': 1930}
{'path': '/home/dohyungkim2023/my-python-repo/scope2.py', 'size': 1444}
{'path': '/home/dohyungkim2023/my-python-repo/fizz-buzz-item.py', 'size': 1203}
{'path': '/home/dohyungkim2023/my-python-repo/wk13-Mon-lesson-04032023.py', 'size': 6904}
{'path': '/home/dohyungkim2023/my-python-repo/using-list.py', 'size': 4017}
{'path': '/home/dohyungkim2023/my-python-repo/variations.py', 'size': 3297}
{'path': '/home/dohyungkim2023/my-python-repo/Hello_world.py', 'size': 53}
{'path': '/home/dohyungkim2023/my-python-repo/Hello_yourname.py', 'size': 1080}
{'path': '/home/dohyungkim2023/my-python-repo/using-generator.py', 'size': 2540}
{'path': '/home/dohyungkim2023/my-python-repo/testing-functions.py', 'size': 4248}
{'path': '/home/dohyungkim2023/my-python-repo/string-info.py', 'size': 2679}
{'path': '/home/dohyungkim2023/my-python-repo/scopes.py', 'size': 2292}
{'path': '/home/dohyungkim2023/my-python-repo/.gitignore', 'size': 1799}
{'path': '/home/dohyungkim2023/my-python-repo/fizz-buzz.py', 'size': 1121}
{'path': '/home/dohyungkim2023/my-python-repo/py-if-elif-else.py', 'size': 1397}
{'path': '/home/dohyungkim2023/my-python-repo/using-dictionaries.py', 'size': 6584}
{'path': '/home/dohyungkim2023/my-python-repo/README.md', 'size': 152}
{'path': '/home/dohyungkim2023/my-python-repo/find_string.py', 'size': 1006}
{'path': '/home/dohyungkim2023/my-python-repo/split&join_again.py', 'size': 1930}
{'path': '/home/dohyungkim2023/my-python-repo/scope2.py', 'size': 1444}
{'path': '/home/dohyungkim2023/my-python-repo/fizz-buzz-item.py', 'size': 1203}
{'path': '/home/dohyungkim2023/my-python-repo/wk13-Mon-lesson-04032023.py', 'size': 6904}
{'path': '/home/dohyungkim2023/my-python-repo/using-list.py', 'size': 4017}
{'path': '/home/dohyungkim2023/my-python-repo/variations.py', 'size': 3297}
{'path': '/home/dohyungkim2023/my-python-repo/Hello_world.py', 'size': 53}
{'path': '/home/dohyungkim2023/my-python-repo/Hello_yourname.py', 'size': 1080}
{'path': '/home/dohyungkim2023/my-python-repo/using-generator.py', 'size': 2540}
{'path': '/home/dohyungkim2023/my-python-repo/.git/index', 'size': 2257}
{'path': '/home/dohyungkim2023/my-python-repo/.git/HEAD', 'size': 30}
{'path': '/home/dohyungkim2023/my-python-repo/.git/packed-refs', 'size': 46}
{'path': '/home/dohyungkim2023/my-python-repo/.git/config', 'size': 263}
{'path': '/home/dohyungkim2023/my-python-repo/.git/description', 'size': 73}
{'path': '/home/dohyungkim2023/my-python-repo/.git/FETCH_HEAD', 'size': 102}
{'path': '/home/dohyungkim2023/my-python-repo/.git/COMMIT_EDITMSG', 'size': 19}
{'path': '/home/dohyungkim2023/my-python-repo/.git/ORIG_HEAD', 'size': 41}
{'path': '/home/dohyungkim2023/my-python-repo/.git/index', 'size': 2257}
{'path': '/home/dohyungkim2023/my-python-repo/.git/HEAD', 'size': 30}
{'path': '/home/dohyungkim2023/my-python-repo/.git/packed-refs', 'size': 46}
{'path': '/home/dohyungkim2023/my-python-repo/.git/config', 'size': 263}
{'path': '/home/dohyungkim2023/my-python-repo/.git/description', 'size': 73}
{'path': '/home/dohyungkim2023/my-python-repo/.git/FETCH_HEAD', 'size': 102}
{'path': '/home/dohyungkim2023/my-python-repo/.git/COMMIT_EDITMSG', 'size': 19}
{'path': '/home/dohyungkim2023/my-python-repo/.git/ORIG_HEAD', 'size': 41}
{'path': '/home/dohyungkim2023/my-python-repo/.git/index', 'size': 2257}
{'path': '/home/dohyungkim2023/my-python-repo/.git/HEAD', 'size': 30}
{'path': '/home/dohyungkim2023/my-python-repo/.git/packed-refs', 'size': 46}
{'path': '/home/dohyungkim2023/my-python-repo/.git/config', 'size': 263}
{'path': '/home/dohyungkim2023/my-python-repo/.git/description', 'size': 73}
{'path': '/home/dohyungkim2023/my-python-repo/.git/FETCH_HEAD', 'size': 102}
{'path': '/home/dohyungkim2023/my-python-repo/.git/COMMIT_EDITMSG', 'size': 19}
{'path': '/home/dohyungkim2023/my-python-repo/.git/ORIG_HEAD', 'size': 41}
{'path': '/home/dohyungkim2023/my-python-repo/.git/index', 'size': 2257}
{'path': '/home/dohyungkim2023/my-python-repo/.git/HEAD', 'size': 30}
{'path': '/home/dohyungkim2023/my-python-repo/.git/packed-refs', 'size': 46}
{'path': '/home/dohyungkim2023/my-python-repo/.git/config', 'size': 263}
{'path': '/home/dohyungkim2023/my-python-repo/.git/description', 'size': 73}
{'path': '/home/dohyungkim2023/my-python-repo/.git/FETCH_HEAD', 'size': 102}
{'path': '/home/dohyungkim2023/my-python-repo/.git/COMMIT_EDITMSG', 'size': 19}
{'path': '/home/dohyungkim2023/my-python-repo/.git/ORIG_HEAD', 'size': 41}
{'path': '/home/dohyungkim2023/my-python-repo/.git/index', 'size': 2257}
{'path': '/home/dohyungkim2023/my-python-repo/.git/HEAD', 'size': 30}
{'path': '/home/dohyungkim2023/my-python-repo/.git/packed-refs', 'size': 46}
{'path': '/home/dohyungkim2023/my-python-repo/.git/config', 'size': 263}
{'path': '/home/dohyungkim2023/my-python-repo/.git/description', 'size': 73}
{'path': '/home/dohyungkim2023/my-python-repo/.git/FETCH_HEAD', 'size': 102}
{'path': '/home/dohyungkim2023/my-python-repo/.git/COMMIT_EDITMSG', 'size': 19}
{'path': '/home/dohyungkim2023/my-python-repo/.git/ORIG_HEAD', 'size': 41}
{'path': '/home/dohyungkim2023/my-python-repo/.git/index', 'size': 2257}
{'path': '/home/dohyungkim2023/my-python-repo/.git/HEAD', 'size': 30}
{'path': '/home/dohyungkim2023/my-python-repo/.git/packed-refs', 'size': 46}
{'path': '/home/dohyungkim2023/my-python-repo/.git/config', 'size': 263}
{'path': '/home/dohyungkim2023/my-python-repo/.git/description', 'size': 73}
{'path': '/home/dohyungkim2023/my-python-repo/.git/FETCH_HEAD', 'size': 102}
{'path': '/home/dohyungkim2023/my-python-repo/.git/COMMIT_EDITMSG', 'size': 19}
{'path': '/home/dohyungkim2023/my-python-repo/.git/ORIG_HEAD', 'size': 41}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/branches
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/hooks
{'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/fsmonitor-watchman.sample', 'size': 4655}
{'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/push-to-checkout.sample', 'size': 2783}
{'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/update.sample', 'size': 3650}
{'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/pre-applypatch.sample', 'size': 424}
{'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/pre-push.sample', 'size': 1374}
{'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/pre-receive.sample', 'size': 544}
{'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/pre-merge-commit.sample', 'size': 416}
{'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/applypatch-msg.sample', 'size': 478}
{'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/pre-commit.sample', 'size': 1643}
{'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/prepare-commit-msg.sample', 'size': 1492}
{'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/commit-msg.sample', 'size': 896}
{'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/post-update.sample', 'size': 189}
{'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/pre-rebase.sample', 'size': 4898}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/49
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/49/643f1f2687790aa54b9c066a5c303e7b530f0e', 'size': 162}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/52
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/52/8b11654c973a9fd1d30cca7746b1989a84d0aa', 'size': 280}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/c5
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/c5/65835127d3055fd14927dd5644cca075b84dbb', 'size': 165}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/7d
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7d/287af85a3a917e3ae6f4085b44e45d5e9b3e5f', 'size': 186}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7d/928b1ee8ddcdd4d2de61219b9d48190e57f26d', 'size': 517}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/e3
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e3/3d9011c1307a3d6eceb5a796be9a7121fcb329', 'size': 1364}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e3/e83ecd35e8f75eca5b4400a320ad0c27cf0ec4', 'size': 177}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/7c
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7c/68f4aafcb40a040100f86f122148d1765c1abd', 'size': 190}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/ad
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/ad/0bfc9860c05866da5cb074379abb189a3f38d8', 'size': 746}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/a2
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/a2/b1fde369283c0aae5847fba2e635d666112091', 'size': 588}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/44
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/44/e91f48ddd90ca5b30ca4b6d07f3b48fcc496ab', 'size': 1115}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/3e
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/3e/02c256775bfba9516bdb6a69f2dea5e0d54399', 'size': 517}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/30
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/30/bdfd802123c72180ef2a02dc80b729be4b84ca', 'size': 174}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/f5
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/f5/b1518f34f1473117f1170e96e86345190c8d33', 'size': 188}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/5b
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/5b/b4097d5112118577f618488f29e59fa1990241', 'size': 189}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/5b/836af98a0821787f2a7b8292535a27cc6d088c', 'size': 467}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/b4
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b4/fd8f400b07573940da882f5f1f69856057be3e', 'size': 552}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/b0
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b0/db908dc9b902458ca3619f65bbf31c0174c3d1', 'size': 773}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b0/ec75214984034f96d9d20ccab1a475a83aca7e', 'size': 1508}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/51
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/51/ffc52f125dbfefa6669a2371b39ff0c76b1695', 'size': 175}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/a8
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/a8/5225a0ce546492e8138a283873e50512268044', 'size': 646}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/a8/4021b0641b86c33c748a40f0a3517e182486da', 'size': 757}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/bd
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/bd/3aba3c41e36b11d0605ee91f2b8940950f65aa', 'size': 195}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/6b
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/6b/426a519a7a65f7aef9bfa9a60f7200ac7e2124', 'size': 274}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/55
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/55/189ea76ed6d6f154245f467346675d966916fd', 'size': 1187}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/55/48d1e3a25e1ab5793b8651d894f29296cee398', 'size': 186}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/86
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/86/0c00594ae75ca8ec2f1ecbc21dd1b06bff69b4', 'size': 645}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/df
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/df/fca6d33fde52fb73d66cb2cec201641fb22a8c', 'size': 5616}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/8b
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/8b/9201506d17e10935cab341abf3403fc0fab1df', 'size': 192}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/07
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/07/081d9d3778d79f8358839d337d7362bfc1fa4d', 'size': 168}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/15
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/15/1309920de6d161f251f4f527f2e2ba5a784d53', 'size': 372}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/15/a1d717d75979fd412b3faed51f4cb34740c2dc', 'size': 713}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/1e
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/1e/3caea0585fc90c7f1d1a4cd9a6b0b1619a1336', 'size': 460}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/79
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/79/b04af55b52006dd4e77e9f7b1c58690601e941', 'size': 548}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/bb
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/bb/1ba790a3ca1a2de7cdccb5942617e1ace6bd58', 'size': 181}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/24
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/24/206c4d129cc3ca3fa03aa204a14de820609e02', 'size': 879}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/6a
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/6a/a6d559918d3a22f38b8628f9a685bcd720b90e', 'size': 1425}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/3b
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/3b/fba49af95e18b2a96a64661c7b7c5a043733cb', 'size': 339}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/12
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/12/1101ae5553a457bc5ea51c393683c5bc819af2', 'size': 754}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/bc
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/bc/db0c253e3122380a94bb72f97af683a5f221d6', 'size': 645}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/f2
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/f2/2c338f4806a135e349a35aa89d3b65aa1e9266', 'size': 2839}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/pack
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/pack/pack-c2f6c395361081eacaa8ad99cdd5b6ee71fe9e7a.pack', 'size': 47586}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/pack/pack-c2f6c395361081eacaa8ad99cdd5b6ee71fe9e7a.idx', 'size': 9696}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/39
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/39/0fc4105e38ad77ba4af26915c7c8c4938116a1', 'size': 648}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/fe
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/fe/dd72890cd1e67ceb128ada17d74dc9a9e48e8d', 'size': 174}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/fe/fa9d82db3038e37b1b66188665adf819761497', 'size': 714}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/fe/e918db9d682b5b72afaa0380ffc308e95b1fe6', 'size': 630}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/cf
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/cf/68c5c767b37ca1da86e7ef7787179bb9f92d3d', 'size': 713}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/89
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/89/d2d529acb7b3eec35eb253eaad3d2d560561ea', 'size': 175}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/56
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/56/8059592871c1af40ab29184ee72ac1b4fa6256', 'size': 706}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/a9
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/a9/39dcfb58ea56b075d0d9a20e04ccad0680aade', 'size': 649}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/a9/b715aa58581aae109876cd4b943834b53da2e0', 'size': 727}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/5c
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/5c/592fd7f7d3d6f0aefc6c7e6e45d1ec530057ef', 'size': 793}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/5c/629f6f736c2399279ee7ab0bc2d28fb15fec70', 'size': 659}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/db
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/db/ff3b0ede55191a9c1794f1b16caeb0f512851c', 'size': 186}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/db/c5e624e52b3600f60321ed9c01220f760d2940', 'size': 166}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/db/c8ad028bf4647fb621e5a836c421a805c3c897', 'size': 166}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/f8
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/f8/d5d1c35d69a126e0f0d00b2e18fded21dae18a', 'size': 10391}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/f8/3488d50435da081d04272f8a9f421c3fca0024', 'size': 627}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/61
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/61/563060fd251ec7a59f7640627f4ac9be965f8a', 'size': 517}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/8f
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/8f/04b5aa8d81b80c98310a7de08e971449a67465', 'size': 517}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/8f/b0f0ab6204966eafa3ca4eb4c160c1ff655cf4', 'size': 237}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/d0
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/d0/ba861cd519bce06732c63c594dc2fe151c6ac8', 'size': 679}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/fd
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/fd/84e220aadc3997f7fd9e692da8b989cf4ea523', 'size': 517}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/2e
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/2e/8b658b034ee863a505ac60f69e93833f0dfeae', 'size': 631}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/77
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/77/af61b5e0da01cdf7ee65a51cff5126cc22c05c', 'size': 754}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/e1
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e1/0b9e03b8b4ded7022d28f13cad3a5234ec0a8b', 'size': 1069}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/a4
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/a4/2a34aee20dd0cc48cb07380cc1185e3ae34e69', 'size': 268}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/05
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/05/24cbdcd374d58f9fe916af757873132f7ee761', 'size': 13784}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/cd
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/cd/2628560a9c20fbf5bde25ad75df07717bc44ee', 'size': 588}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/cd/57ec51d6528b92ae854c39797800a56793ba0f', 'size': 1437}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/4e
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/4e/56e999470e8fea5b33bf166521043e61ebf21a', 'size': 185}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/57
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/57/39ca7bcd15400233caba1c2837324eff0581a2', 'size': 640}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/1f
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/1f/17d9d2aa9216156ec305041b4af962f33c0324', 'size': 2171}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/2d
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/2d/feca495a97bbe68f80ead23b9a180b3f016b4f', 'size': 1338}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/7a
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7a/a14c719238ba6ab4ad189959c7139b1b673aed', 'size': 12380}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7a/0e4e6490879ab51ab5f950c3b163ea3942a713', 'size': 746}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/9a
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/9a/da4f7af78af440a5dbffd659b8c07b69d9deb6', 'size': 13782}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/9a/1d7c1c1cd9e40f56809a9f602d4dc7f65c30ff', 'size': 746}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/d1
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/d1/c9460bbfe8ed3998144c61e3cad22476ea9196', 'size': 175}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/d1/54061b8c4e2c477e239d3a3b4cc1091bdece75', 'size': 790}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/11
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/11/34d4c525753dbf2b7b67c6a2dbbcbcc5141dc5', 'size': 162}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/11/2e3fa45e7a3066403586af9c8b732298cbf2fb', 'size': 754}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/4a
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/4a/21f73359a1041ee825a3b90a221737df66360a', 'size': 182}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/04
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/04/4ace1ce598045b3f6e144b86a363938e468d22', 'size': 713}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/ef
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/ef/1d0aa6c117b712c88f5f5b85b8785878abec21', 'size': 172}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/ef/770e80243fa8b983b7c460ae10fa8f94080a16', 'size': 180}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/91
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/91/445d045d48af5ac657eb4e57236affbf957319', 'size': 848}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/70
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/70/f87e88c40362500f354d5ba0cb19c36ff9dffd', 'size': 165}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/70/efc0e9308124404b7dac3bf1d18514f7497fbc', 'size': 168}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/7e
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7e/2eac4fb2c2b50ddfdedc3be41fa57dbeb0bd89', 'size': 708}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7e/94229fabe95566121299ecdc96732378999a5d', 'size': 171}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/3f
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/3f/8acedfc8c2781a22bf6f359bcee9345750f6ed', 'size': 83810}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/de
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/de/b2b7dffe81dae9747eaf28d555227390a4eef4', 'size': 517}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/0e
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/0e/397a5bac8d47df962c710719e7f79d31769787', 'size': 175}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/4d
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/4d/0cad273b78f9ce5ec8cfa7223ef02804a46d33', 'size': 517}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/f3
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/f3/00cd16db6b883fa518abd447da5711734553dc', 'size': 165}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/b2
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b2/42bdcca03f0488714b078cd0005f8bccc634a6', 'size': 81}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/85
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/85/24c6b4b47627abea364661a1e10821e5e5060f', 'size': 713}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/85/f5a01de7c56e79c5ae50edc6dcb9a0cb048aa6', 'size': 1230}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/03
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/03/4b92b1e2ff5ad46af3aaa6b07c453da225dc06', 'size': 261}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/60
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/60/ee7ff66a4e24815a19ab6a15bead0e47157c4a', 'size': 2184}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/60/f9e859e5263392d33b03497072e861a6a50e47', 'size': 176}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/ba
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/ba/5a2aebfef323fff7e8b5f3d097c4e06a75f40e', 'size': 2806}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/ec
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/ec/da58750c3637d01fc9f560f74c6998fca70450', 'size': 899}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/ec/b7ec65bb946cc74c9d4f7cfe465d382c988cfa', 'size': 531}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/ea
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/ea/e7f62b0516c65b4bc8a47a1fe1b78707057e35', 'size': 746}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/09
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/09/b012e77630215158a34813ad624b4691a1a986', 'size': 807}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/80
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/80/e20920fb732fa585230f43947b322d1799ac9f', 'size': 615}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/67
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/67/1b28ccee7ddae70faa0a53eb0781d189d65c42', 'size': 649}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/a7
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/a7/21c62629648d6caefd3d5f6e19580730d96413', 'size': 164}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/1d
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/1d/bba33dac22c791e86c3ccfa51c9b16f082f02a', 'size': 187}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/13
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/13/d8f8378b80496f778fd5c2660bcaa9fceb0a8c', 'size': 175}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/13/24716327e824d34d0e3ad907d1c27729b2dd1f', 'size': 1183}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/32
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/32/696ee6c5b102d64d16df6e768cb99b0b35926a', 'size': 517}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/32/8d69ce0d59c5175ff58b47e87325ae3e3b52d5', 'size': 1238}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/info
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/b6
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b6/779320394da6f4484bc926683d21ac41196b54', 'size': 1179}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b6/f777725f0000abc51738efdbd413deaee48e36', 'size': 176}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/e8
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e8/bfcf8ce4f9be67019cedb45f1b5265693f6e18', 'size': 175}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/26
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/26/c3a1c490466b6d9e9aa65b04b8e02f34d13a0b', 'size': 615}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/b1
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b1/9c779b1749ef6badecbc74a6e2b3646bbf790a', 'size': 687}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b1/336a948e9eb6a9d3eb06c93e287ff6f1d0d91c', 'size': 624}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/1b
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/1b/fcb3f5f9d27524136b744d4a6b907e412ee5ab', 'size': 469}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/e0
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e0/fdef9563b110ef1925bfa6544acb10cf16fbc2', 'size': 889}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/0c
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/0c/fc551ba8c25d1330b421d22b2b2125ee5d8a6f', 'size': 140}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/5d
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/5d/49ebb685c5b602a58d909b7d7bb4949542a48b', 'size': 320}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/5d/b10daf8245892c7fe874dffe59abe45ef12d78', 'size': 2284}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/1a
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/1a/a0a95110d1c19e9de7308d2e3ffb2594faa6e3', 'size': 232}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/7b
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7b/1cc34cff9ff511d166ad4b71dd0e052ac8fb1d', 'size': 166}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7b/11c8c687a57780b9baf1038cc22efbd9f78422', 'size': 178}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/e7
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e7/abc8b9014da7209cf242c1ff948e8feddc23b8', 'size': 171}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/fc
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/fc/52f07c3c82b3df2deaf49200ab2a56c14175f8', 'size': 552}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/fc/a03bab2fcd8d039a7998af59a15f3de173f8c0', 'size': 547}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/d9
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/d9/fea6ac86159840757f30565dbda375e79ba39f', 'size': 1244}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/6c
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/6c/5f11fcb426454c02847c6b795354fff776cab4', 'size': 713}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/eb
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/eb/01d12a6335d005c5276a8d2dc634452a64bd1c', 'size': 1011}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/84
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/84/d41bc3d2fbc8faa86f8b4dfed887b412a4b92b', 'size': 189}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/e5
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e5/309aa67ed69b926490a44f0b6b76518b64ee29', 'size': 632}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/54
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/54/402fbf718bdccd6231740f7db1a192dd0b49d5', 'size': 925}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/c8
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/c8/b8bf481cc58a43b4927caf04c4bdb0e1d58da6', 'size': 2514}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/38
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/38/6838c905ce704e33c4eaa205211714ed9e0e39', 'size': 551}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/17
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/17/61e3eff0243b7c3f93f1846e38c635540200e1', 'size': 496}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/c2
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/c2/ae9d8e619633e3611372b6a7c6ebd979cc56a9', 'size': 587}
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/c2/e33ef95f6f2cb20dabaa77274576ff984f4b49', 'size': 616}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/62
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/62/b69a0aedacf895ce57c84e7331500a04c12097', 'size': 650}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/b7
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b7/ebfcccb1369a2d8828ca0c77080a7d3a33dfc6', 'size': 647}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/6e
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/6e/540a6c0e7ca18ec97fd1e5d6d3be3577422572', 'size': 166}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/objects/e9
{'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e9/d85e4cc767f8c076c9498b9d2b618a357384ca', 'size': 642}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/info
{'path': '/home/dohyungkim2023/my-python-repo/.git/info/exclude', 'size': 240}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/refs/tags
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/refs/remotes/origin
{'path': '/home/dohyungkim2023/my-python-repo/.git/refs/remotes/origin/main', 'size': 41}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/refs/heads
{'path': '/home/dohyungkim2023/my-python-repo/.git/refs/heads/main', 'size': 41}
{'path': '/home/dohyungkim2023/my-python-repo/.git/refs/heads/dkim-04102023', 'size': 41}
{'path': '/home/dohyungkim2023/my-python-repo/.git/logs/HEAD', 'size': 13077}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes/origin
{'path': '/home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes/origin/main', 'size': 1960}
This is the directory of  /home/dohyungkim2023/my-python-repo/.git/logs/refs/heads
{'path': '/home/dohyungkim2023/my-python-repo/.git/logs/refs/heads/main', 'size': 3292}
{'path': '/home/dohyungkim2023/my-python-repo/.git/logs/refs/heads/dkim-04102023', 'size': 506}
This is the directory of  /home/dohyungkim2023/my-python-repo/week13
{'path': '/home/dohyungkim2023/my-python-repo/week13/wk13-project_walk_fd_v3.py', 'size': 83543}
{'path': '/home/dohyungkim2023/my-python-repo/week13/wk13-project_list_v1.py', 'size': 1471}
{'path': '/home/dohyungkim2023/my-python-repo/week13/wk13-project_walk_fd.py', 'size': 16044}
{'path': '/home/dohyungkim2023/my-python-repo/week13/wk13-project_file_dict_1st_draft.py', 'size': 3745}
{'path': '/home/dohyungkim2023/my-python-repo/week13/wk13-project_walk_fd_v2.py', 'size': 1817}
{'path': '/home/dohyungkim2023/my-python-repo/week13/output.txt', 'size': 487529}
{'path': '/home/dohyungkim2023/my-python-repo/week13/wk13-project_walk_fd_v3_rev1.py', 'size': 68590}
This is the directory of  /home/dohyungkim2023/my-python-repo/week12
{'path': '/home/dohyungkim2023/my-python-repo/week12/wk12-project_AWS-service-inventory.py', 'size': 6779}
[{'path': '/home/dohyungkim2023/my-python-repo/testing-functions.py', 'size': 4248}, {'path': '/home/dohyungkim2023/my-python-repo/string-info.py', 'size': 2679}, {'path': '/home/dohyungkim2023/my-python-repo/scopes.py', 'size': 2292}, {'path': '/home/dohyungkim2023/my-python-repo/.gitignore', 'size': 1799}, {'path': '/home/dohyungkim2023/my-python-repo/fizz-buzz.py', 'size': 1121}, {'path': '/home/dohyungkim2023/my-python-repo/py-if-elif-else.py', 'size': 1397}, {'path': '/home/dohyungkim2023/my-python-repo/using-dictionaries.py', 'size': 6584}, {'path': '/home/dohyungkim2023/my-python-repo/README.md', 'size': 152}, {'path': '/home/dohyungkim2023/my-python-repo/find_string.py', 'size': 1006}, {'path': '/home/dohyungkim2023/my-python-repo/split&join_again.py', 'size': 1930}, {'path': '/home/dohyungkim2023/my-python-repo/scope2.py', 'size': 1444}, {'path': '/home/dohyungkim2023/my-python-repo/fizz-buzz-item.py', 'size': 1203}, {'path': '/home/dohyungkim2023/my-python-repo/wk13-Mon-lesson-04032023.py', 'size': 6904}, {'path': '/home/dohyungkim2023/my-python-repo/using-list.py', 'size': 4017}, {'path': '/home/dohyungkim2023/my-python-repo/variations.py', 'size': 3297}, {'path': '/home/dohyungkim2023/my-python-repo/Hello_world.py', 'size': 53}, {'path': '/home/dohyungkim2023/my-python-repo/Hello_yourname.py', 'size': 1080}, {'path': '/home/dohyungkim2023/my-python-repo/using-generator.py', 'size': 2540}, {'path': '/home/dohyungkim2023/my-python-repo/testing-functions.py', 'size': 4248}, {'path': '/home/dohyungkim2023/my-python-repo/string-info.py', 'size': 2679}, {'path': '/home/dohyungkim2023/my-python-repo/scopes.py', 'size': 2292}, {'path': '/home/dohyungkim2023/my-python-repo/.gitignore', 'size': 1799}, {'path': '/home/dohyungkim2023/my-python-repo/fizz-buzz.py', 'size': 1121}, {'path': '/home/dohyungkim2023/my-python-repo/py-if-elif-else.py', 'size': 1397}, {'path': '/home/dohyungkim2023/my-python-repo/using-dictionaries.py', 'size': 6584}, {'path': '/home/dohyungkim2023/my-python-repo/README.md', 'size': 152}, {'path': '/home/dohyungkim2023/my-python-repo/find_string.py', 'size': 1006}, {'path': '/home/dohyungkim2023/my-python-repo/split&join_again.py', 'size': 1930}, {'path': '/home/dohyungkim2023/my-python-repo/scope2.py', 'size': 1444}, {'path': '/home/dohyungkim2023/my-python-repo/fizz-buzz-item.py', 'size': 1203}, {'path': '/home/dohyungkim2023/my-python-repo/wk13-Mon-lesson-04032023.py', 'size': 6904}, {'path': '/home/dohyungkim2023/my-python-repo/using-list.py', 'size': 4017}, {'path': '/home/dohyungkim2023/my-python-repo/variations.py', 'size': 3297}, {'path': '/home/dohyungkim2023/my-python-repo/Hello_world.py', 'size': 53}, {'path': '/home/dohyungkim2023/my-python-repo/Hello_yourname.py', 'size': 1080}, {'path': '/home/dohyungkim2023/my-python-repo/using-generator.py', 'size': 2540}, {'path': '/home/dohyungkim2023/my-python-repo/testing-functions.py', 'size': 4248}, {'path': '/home/dohyungkim2023/my-python-repo/string-info.py', 'size': 2679}, {'path': '/home/dohyungkim2023/my-python-repo/scopes.py', 'size': 2292}, {'path': '/home/dohyungkim2023/my-python-repo/.gitignore', 'size': 1799}, {'path': '/home/dohyungkim2023/my-python-repo/fizz-buzz.py', 'size': 1121}, {'path': '/home/dohyungkim2023/my-python-repo/py-if-elif-else.py', 'size': 1397}, {'path': '/home/dohyungkim2023/my-python-repo/using-dictionaries.py', 'size': 6584}, {'path': '/home/dohyungkim2023/my-python-repo/README.md', 'size': 152}, {'path': '/home/dohyungkim2023/my-python-repo/find_string.py', 'size': 1006}, {'path': '/home/dohyungkim2023/my-python-repo/split&join_again.py', 'size': 1930}, {'path': '/home/dohyungkim2023/my-python-repo/scope2.py', 'size': 1444}, {'path': '/home/dohyungkim2023/my-python-repo/fizz-buzz-item.py', 'size': 1203}, {'path': '/home/dohyungkim2023/my-python-repo/wk13-Mon-lesson-04032023.py', 'size': 6904}, {'path': '/home/dohyungkim2023/my-python-repo/using-list.py', 'size': 4017}, {'path': '/home/dohyungkim2023/my-python-repo/variations.py', 'size': 3297}, {'path': '/home/dohyungkim2023/my-python-repo/Hello_world.py', 'size': 53}, {'path': '/home/dohyungkim2023/my-python-repo/Hello_yourname.py', 'size': 1080}, {'path': '/home/dohyungkim2023/my-python-repo/using-generator.py', 'size': 2540}, {'path': '/home/dohyungkim2023/my-python-repo/.git/index', 'size': 2257}, {'path': '/home/dohyungkim2023/my-python-repo/.git/HEAD', 'size': 30}, {'path': '/home/dohyungkim2023/my-python-repo/.git/packed-refs', 'size': 46}, {'path': '/home/dohyungkim2023/my-python-repo/.git/config', 'size': 263}, {'path': '/home/dohyungkim2023/my-python-repo/.git/description', 'size': 73}, {'path': '/home/dohyungkim2023/my-python-repo/.git/FETCH_HEAD', 'size': 102}, {'path': '/home/dohyungkim2023/my-python-repo/.git/COMMIT_EDITMSG', 'size': 19}, {'path': '/home/dohyungkim2023/my-python-repo/.git/ORIG_HEAD', 'size': 41}, {'path': '/home/dohyungkim2023/my-python-repo/.git/index', 'size': 2257}, {'path': '/home/dohyungkim2023/my-python-repo/.git/HEAD', 'size': 30}, {'path': '/home/dohyungkim2023/my-python-repo/.git/packed-refs', 'size': 46}, {'path': '/home/dohyungkim2023/my-python-repo/.git/config', 'size': 263}, {'path': '/home/dohyungkim2023/my-python-repo/.git/description', 'size': 73}, {'path': '/home/dohyungkim2023/my-python-repo/.git/FETCH_HEAD', 'size': 102}, {'path': '/home/dohyungkim2023/my-python-repo/.git/COMMIT_EDITMSG', 'size': 19}, {'path': '/home/dohyungkim2023/my-python-repo/.git/ORIG_HEAD', 'size': 41}, {'path': '/home/dohyungkim2023/my-python-repo/.git/index', 'size': 2257}, {'path': '/home/dohyungkim2023/my-python-repo/.git/HEAD', 'size': 30}, {'path': '/home/dohyungkim2023/my-python-repo/.git/packed-refs', 'size': 46}, {'path': '/home/dohyungkim2023/my-python-repo/.git/config', 'size': 263}, {'path': '/home/dohyungkim2023/my-python-repo/.git/description', 'size': 73}, {'path': '/home/dohyungkim2023/my-python-repo/.git/FETCH_HEAD', 'size': 102}, {'path': '/home/dohyungkim2023/my-python-repo/.git/COMMIT_EDITMSG', 'size': 19}, {'path': '/home/dohyungkim2023/my-python-repo/.git/ORIG_HEAD', 'size': 41}, {'path': '/home/dohyungkim2023/my-python-repo/.git/index', 'size': 2257}, {'path': '/home/dohyungkim2023/my-python-repo/.git/HEAD', 'size': 30}, {'path': '/home/dohyungkim2023/my-python-repo/.git/packed-refs', 'size': 46}, {'path': '/home/dohyungkim2023/my-python-repo/.git/config', 'size': 263}, {'path': '/home/dohyungkim2023/my-python-repo/.git/description', 'size': 73}, {'path': '/home/dohyungkim2023/my-python-repo/.git/FETCH_HEAD', 'size': 102}, {'path': '/home/dohyungkim2023/my-python-repo/.git/COMMIT_EDITMSG', 'size': 19}, {'path': '/home/dohyungkim2023/my-python-repo/.git/ORIG_HEAD', 'size': 41}, {'path': '/home/dohyungkim2023/my-python-repo/.git/index', 'size': 2257}, {'path': '/home/dohyungkim2023/my-python-repo/.git/HEAD', 'size': 30}, {'path': '/home/dohyungkim2023/my-python-repo/.git/packed-refs', 'size': 46}, {'path': '/home/dohyungkim2023/my-python-repo/.git/config', 'size': 263}, {'path': '/home/dohyungkim2023/my-python-repo/.git/description', 'size': 73}, {'path': '/home/dohyungkim2023/my-python-repo/.git/FETCH_HEAD', 'size': 102}, {'path': '/home/dohyungkim2023/my-python-repo/.git/COMMIT_EDITMSG', 'size': 19}, {'path': '/home/dohyungkim2023/my-python-repo/.git/ORIG_HEAD', 'size': 41}, {'path': '/home/dohyungkim2023/my-python-repo/.git/index', 'size': 2257}, {'path': '/home/dohyungkim2023/my-python-repo/.git/HEAD', 'size': 30}, {'path': '/home/dohyungkim2023/my-python-repo/.git/packed-refs', 'size': 46}, {'path': '/home/dohyungkim2023/my-python-repo/.git/config', 'size': 263}, {'path': '/home/dohyungkim2023/my-python-repo/.git/description', 'size': 73}, {'path': '/home/dohyungkim2023/my-python-repo/.git/FETCH_HEAD', 'size': 102}, {'path': '/home/dohyungkim2023/my-python-repo/.git/COMMIT_EDITMSG', 'size': 19}, {'path': '/home/dohyungkim2023/my-python-repo/.git/ORIG_HEAD', 'size': 41}, {'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/fsmonitor-watchman.sample', 'size': 4655}, {'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/push-to-checkout.sample', 'size': 2783}, {'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/update.sample', 'size': 3650}, {'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/pre-applypatch.sample', 'size': 424}, {'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/pre-push.sample', 'size': 1374}, {'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/pre-receive.sample', 'size': 544}, {'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/pre-merge-commit.sample', 'size': 416}, {'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/applypatch-msg.sample', 'size': 478}, {'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/pre-commit.sample', 'size': 1643}, {'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/prepare-commit-msg.sample', 'size': 1492}, {'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/commit-msg.sample', 'size': 896}, {'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/post-update.sample', 'size': 189}, {'path': '/home/dohyungkim2023/my-python-repo/.git/hooks/pre-rebase.sample', 'size': 4898}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/49/643f1f2687790aa54b9c066a5c303e7b530f0e', 'size': 162}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/52/8b11654c973a9fd1d30cca7746b1989a84d0aa', 'size': 280}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/c5/65835127d3055fd14927dd5644cca075b84dbb', 'size': 165}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7d/287af85a3a917e3ae6f4085b44e45d5e9b3e5f', 'size': 186}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7d/928b1ee8ddcdd4d2de61219b9d48190e57f26d', 'size': 517}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e3/3d9011c1307a3d6eceb5a796be9a7121fcb329', 'size': 1364}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e3/e83ecd35e8f75eca5b4400a320ad0c27cf0ec4', 'size': 177}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7c/68f4aafcb40a040100f86f122148d1765c1abd', 'size': 190}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/ad/0bfc9860c05866da5cb074379abb189a3f38d8', 'size': 746}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/a2/b1fde369283c0aae5847fba2e635d666112091', 'size': 588}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/44/e91f48ddd90ca5b30ca4b6d07f3b48fcc496ab', 'size': 1115}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/3e/02c256775bfba9516bdb6a69f2dea5e0d54399', 'size': 517}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/30/bdfd802123c72180ef2a02dc80b729be4b84ca', 'size': 174}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/f5/b1518f34f1473117f1170e96e86345190c8d33', 'size': 188}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/5b/b4097d5112118577f618488f29e59fa1990241', 'size': 189}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/5b/836af98a0821787f2a7b8292535a27cc6d088c', 'size': 467}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b4/fd8f400b07573940da882f5f1f69856057be3e', 'size': 552}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b0/db908dc9b902458ca3619f65bbf31c0174c3d1', 'size': 773}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b0/ec75214984034f96d9d20ccab1a475a83aca7e', 'size': 1508}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/51/ffc52f125dbfefa6669a2371b39ff0c76b1695', 'size': 175}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/a8/5225a0ce546492e8138a283873e50512268044', 'size': 646}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/a8/4021b0641b86c33c748a40f0a3517e182486da', 'size': 757}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/bd/3aba3c41e36b11d0605ee91f2b8940950f65aa', 'size': 195}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/6b/426a519a7a65f7aef9bfa9a60f7200ac7e2124', 'size': 274}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/55/189ea76ed6d6f154245f467346675d966916fd', 'size': 1187}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/55/48d1e3a25e1ab5793b8651d894f29296cee398', 'size': 186}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/86/0c00594ae75ca8ec2f1ecbc21dd1b06bff69b4', 'size': 645}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/df/fca6d33fde52fb73d66cb2cec201641fb22a8c', 'size': 5616}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/8b/9201506d17e10935cab341abf3403fc0fab1df', 'size': 192}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/07/081d9d3778d79f8358839d337d7362bfc1fa4d', 'size': 168}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/15/1309920de6d161f251f4f527f2e2ba5a784d53', 'size': 372}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/15/a1d717d75979fd412b3faed51f4cb34740c2dc', 'size': 713}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/1e/3caea0585fc90c7f1d1a4cd9a6b0b1619a1336', 'size': 460}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/79/b04af55b52006dd4e77e9f7b1c58690601e941', 'size': 548}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/bb/1ba790a3ca1a2de7cdccb5942617e1ace6bd58', 'size': 181}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/24/206c4d129cc3ca3fa03aa204a14de820609e02', 'size': 879}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/6a/a6d559918d3a22f38b8628f9a685bcd720b90e', 'size': 1425}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/3b/fba49af95e18b2a96a64661c7b7c5a043733cb', 'size': 339}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/12/1101ae5553a457bc5ea51c393683c5bc819af2', 'size': 754}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/bc/db0c253e3122380a94bb72f97af683a5f221d6', 'size': 645}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/f2/2c338f4806a135e349a35aa89d3b65aa1e9266', 'size': 2839}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/pack/pack-c2f6c395361081eacaa8ad99cdd5b6ee71fe9e7a.pack', 'size': 47586}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/pack/pack-c2f6c395361081eacaa8ad99cdd5b6ee71fe9e7a.idx', 'size': 9696}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/39/0fc4105e38ad77ba4af26915c7c8c4938116a1', 'size': 648}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/fe/dd72890cd1e67ceb128ada17d74dc9a9e48e8d', 'size': 174}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/fe/fa9d82db3038e37b1b66188665adf819761497', 'size': 714}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/fe/e918db9d682b5b72afaa0380ffc308e95b1fe6', 'size': 630}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/cf/68c5c767b37ca1da86e7ef7787179bb9f92d3d', 'size': 713}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/89/d2d529acb7b3eec35eb253eaad3d2d560561ea', 'size': 175}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/56/8059592871c1af40ab29184ee72ac1b4fa6256', 'size': 706}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/a9/39dcfb58ea56b075d0d9a20e04ccad0680aade', 'size': 649}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/a9/b715aa58581aae109876cd4b943834b53da2e0', 'size': 727}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/5c/592fd7f7d3d6f0aefc6c7e6e45d1ec530057ef', 'size': 793}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/5c/629f6f736c2399279ee7ab0bc2d28fb15fec70', 'size': 659}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/db/ff3b0ede55191a9c1794f1b16caeb0f512851c', 'size': 186}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/db/c5e624e52b3600f60321ed9c01220f760d2940', 'size': 166}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/db/c8ad028bf4647fb621e5a836c421a805c3c897', 'size': 166}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/f8/d5d1c35d69a126e0f0d00b2e18fded21dae18a', 'size': 10391}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/f8/3488d50435da081d04272f8a9f421c3fca0024', 'size': 627}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/61/563060fd251ec7a59f7640627f4ac9be965f8a', 'size': 517}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/8f/04b5aa8d81b80c98310a7de08e971449a67465', 'size': 517}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/8f/b0f0ab6204966eafa3ca4eb4c160c1ff655cf4', 'size': 237}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/d0/ba861cd519bce06732c63c594dc2fe151c6ac8', 'size': 679}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/fd/84e220aadc3997f7fd9e692da8b989cf4ea523', 'size': 517}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/2e/8b658b034ee863a505ac60f69e93833f0dfeae', 'size': 631}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/77/af61b5e0da01cdf7ee65a51cff5126cc22c05c', 'size': 754}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e1/0b9e03b8b4ded7022d28f13cad3a5234ec0a8b', 'size': 1069}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/a4/2a34aee20dd0cc48cb07380cc1185e3ae34e69', 'size': 268}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/05/24cbdcd374d58f9fe916af757873132f7ee761', 'size': 13784}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/cd/2628560a9c20fbf5bde25ad75df07717bc44ee', 'size': 588}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/cd/57ec51d6528b92ae854c39797800a56793ba0f', 'size': 1437}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/4e/56e999470e8fea5b33bf166521043e61ebf21a', 'size': 185}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/57/39ca7bcd15400233caba1c2837324eff0581a2', 'size': 640}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/1f/17d9d2aa9216156ec305041b4af962f33c0324', 'size': 2171}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/2d/feca495a97bbe68f80ead23b9a180b3f016b4f', 'size': 1338}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7a/a14c719238ba6ab4ad189959c7139b1b673aed', 'size': 12380}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7a/0e4e6490879ab51ab5f950c3b163ea3942a713', 'size': 746}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/9a/da4f7af78af440a5dbffd659b8c07b69d9deb6', 'size': 13782}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/9a/1d7c1c1cd9e40f56809a9f602d4dc7f65c30ff', 'size': 746}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/d1/c9460bbfe8ed3998144c61e3cad22476ea9196', 'size': 175}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/d1/54061b8c4e2c477e239d3a3b4cc1091bdece75', 'size': 790}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/11/34d4c525753dbf2b7b67c6a2dbbcbcc5141dc5', 'size': 162}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/11/2e3fa45e7a3066403586af9c8b732298cbf2fb', 'size': 754}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/4a/21f73359a1041ee825a3b90a221737df66360a', 'size': 182}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/04/4ace1ce598045b3f6e144b86a363938e468d22', 'size': 713}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/ef/1d0aa6c117b712c88f5f5b85b8785878abec21', 'size': 172}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/ef/770e80243fa8b983b7c460ae10fa8f94080a16', 'size': 180}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/91/445d045d48af5ac657eb4e57236affbf957319', 'size': 848}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/70/f87e88c40362500f354d5ba0cb19c36ff9dffd', 'size': 165}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/70/efc0e9308124404b7dac3bf1d18514f7497fbc', 'size': 168}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7e/2eac4fb2c2b50ddfdedc3be41fa57dbeb0bd89', 'size': 708}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7e/94229fabe95566121299ecdc96732378999a5d', 'size': 171}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/3f/8acedfc8c2781a22bf6f359bcee9345750f6ed', 'size': 83810}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/de/b2b7dffe81dae9747eaf28d555227390a4eef4', 'size': 517}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/0e/397a5bac8d47df962c710719e7f79d31769787', 'size': 175}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/4d/0cad273b78f9ce5ec8cfa7223ef02804a46d33', 'size': 517}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/f3/00cd16db6b883fa518abd447da5711734553dc', 'size': 165}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b2/42bdcca03f0488714b078cd0005f8bccc634a6', 'size': 81}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/85/24c6b4b47627abea364661a1e10821e5e5060f', 'size': 713}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/85/f5a01de7c56e79c5ae50edc6dcb9a0cb048aa6', 'size': 1230}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/03/4b92b1e2ff5ad46af3aaa6b07c453da225dc06', 'size': 261}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/60/ee7ff66a4e24815a19ab6a15bead0e47157c4a', 'size': 2184}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/60/f9e859e5263392d33b03497072e861a6a50e47', 'size': 176}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/ba/5a2aebfef323fff7e8b5f3d097c4e06a75f40e', 'size': 2806}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/ec/da58750c3637d01fc9f560f74c6998fca70450', 'size': 899}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/ec/b7ec65bb946cc74c9d4f7cfe465d382c988cfa', 'size': 531}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/ea/e7f62b0516c65b4bc8a47a1fe1b78707057e35', 'size': 746}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/09/b012e77630215158a34813ad624b4691a1a986', 'size': 807}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/80/e20920fb732fa585230f43947b322d1799ac9f', 'size': 615}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/67/1b28ccee7ddae70faa0a53eb0781d189d65c42', 'size': 649}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/a7/21c62629648d6caefd3d5f6e19580730d96413', 'size': 164}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/1d/bba33dac22c791e86c3ccfa51c9b16f082f02a', 'size': 187}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/13/d8f8378b80496f778fd5c2660bcaa9fceb0a8c', 'size': 175}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/13/24716327e824d34d0e3ad907d1c27729b2dd1f', 'size': 1183}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/32/696ee6c5b102d64d16df6e768cb99b0b35926a', 'size': 517}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/32/8d69ce0d59c5175ff58b47e87325ae3e3b52d5', 'size': 1238}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b6/779320394da6f4484bc926683d21ac41196b54', 'size': 1179}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b6/f777725f0000abc51738efdbd413deaee48e36', 'size': 176}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e8/bfcf8ce4f9be67019cedb45f1b5265693f6e18', 'size': 175}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/26/c3a1c490466b6d9e9aa65b04b8e02f34d13a0b', 'size': 615}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b1/9c779b1749ef6badecbc74a6e2b3646bbf790a', 'size': 687}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b1/336a948e9eb6a9d3eb06c93e287ff6f1d0d91c', 'size': 624}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/1b/fcb3f5f9d27524136b744d4a6b907e412ee5ab', 'size': 469}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e0/fdef9563b110ef1925bfa6544acb10cf16fbc2', 'size': 889}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/0c/fc551ba8c25d1330b421d22b2b2125ee5d8a6f', 'size': 140}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/5d/49ebb685c5b602a58d909b7d7bb4949542a48b', 'size': 320}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/5d/b10daf8245892c7fe874dffe59abe45ef12d78', 'size': 2284}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/1a/a0a95110d1c19e9de7308d2e3ffb2594faa6e3', 'size': 232}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7b/1cc34cff9ff511d166ad4b71dd0e052ac8fb1d', 'size': 166}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/7b/11c8c687a57780b9baf1038cc22efbd9f78422', 'size': 178}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e7/abc8b9014da7209cf242c1ff948e8feddc23b8', 'size': 171}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/fc/52f07c3c82b3df2deaf49200ab2a56c14175f8', 'size': 552}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/fc/a03bab2fcd8d039a7998af59a15f3de173f8c0', 'size': 547}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/d9/fea6ac86159840757f30565dbda375e79ba39f', 'size': 1244}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/6c/5f11fcb426454c02847c6b795354fff776cab4', 'size': 713}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/eb/01d12a6335d005c5276a8d2dc634452a64bd1c', 'size': 1011}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/84/d41bc3d2fbc8faa86f8b4dfed887b412a4b92b', 'size': 189}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e5/309aa67ed69b926490a44f0b6b76518b64ee29', 'size': 632}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/54/402fbf718bdccd6231740f7db1a192dd0b49d5', 'size': 925}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/c8/b8bf481cc58a43b4927caf04c4bdb0e1d58da6', 'size': 2514}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/38/6838c905ce704e33c4eaa205211714ed9e0e39', 'size': 551}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/17/61e3eff0243b7c3f93f1846e38c635540200e1', 'size': 496}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/c2/ae9d8e619633e3611372b6a7c6ebd979cc56a9', 'size': 587}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/c2/e33ef95f6f2cb20dabaa77274576ff984f4b49', 'size': 616}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/62/b69a0aedacf895ce57c84e7331500a04c12097', 'size': 650}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/b7/ebfcccb1369a2d8828ca0c77080a7d3a33dfc6', 'size': 647}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/6e/540a6c0e7ca18ec97fd1e5d6d3be3577422572', 'size': 166}, {'path': '/home/dohyungkim2023/my-python-repo/.git/objects/e9/d85e4cc767f8c076c9498b9d2b618a357384ca', 'size': 642}, {'path': '/home/dohyungkim2023/my-python-repo/.git/info/exclude', 'size': 240}, {'path': '/home/dohyungkim2023/my-python-repo/.git/refs/remotes/origin/main', 'size': 41}, {'path': '/home/dohyungkim2023/my-python-repo/.git/refs/heads/main', 'size': 41}, {'path': '/home/dohyungkim2023/my-python-repo/.git/refs/heads/dkim-04102023', 'size': 41}, {'path': '/home/dohyungkim2023/my-python-repo/.git/logs/HEAD', 'size': 13077}, {'path': '/home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes/origin/main', 'size': 1960}, {'path': '/home/dohyungkim2023/my-python-repo/.git/logs/refs/heads/main', 'size': 3292}, {'path': '/home/dohyungkim2023/my-python-repo/.git/logs/refs/heads/dkim-04102023', 'size': 506}, {'path': '/home/dohyungkim2023/my-python-repo/week13/wk13-project_walk_fd_v3.py', 'size': 83543}, {'path': '/home/dohyungkim2023/my-python-repo/week13/wk13-project_list_v1.py', 'size': 1471}, {'path': '/home/dohyungkim2023/my-python-repo/week13/wk13-project_walk_fd.py', 'size': 16044}, {'path': '/home/dohyungkim2023/my-python-repo/week13/wk13-project_file_dict_1st_draft.py', 'size': 3745}, {'path': '/home/dohyungkim2023/my-python-repo/week13/wk13-project_walk_fd_v2.py', 'size': 1817}, {'path': '/home/dohyungkim2023/my-python-repo/week13/output.txt', 'size': 487529}, {'path': '/home/dohyungkim2023/my-python-repo/week13/wk13-project_walk_fd_v3_rev1.py', 'size': 68590}, {'path': '/home/dohyungkim2023/my-python-repo/week12/wk12-project_AWS-service-inventory.py', 'size': 6779}]

'''

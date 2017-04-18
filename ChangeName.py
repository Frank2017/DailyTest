# _*_ coding:utf-8 _*_
import os


def do_replace(dir_path, name_list, old_pattern, new_pattern):
    """
    replace的具体操作
    :param dir_path: 文件所处的目录
    :param name_list: 子文件的名称列表
    :param old_pattern: 待匹配的原始字符串
    :param new_pattern: 匹配成功后修改的字符串
    """
    for c in name_list:
        if os.path.isfile(os.path.join(dir_path, c)):  # and c.find(new_pattern) < 0
            # 判断old_pattern是否是list
            if isinstance(old_pattern, list):
                for i in range(len(old_pattern)):
                    # 当old_pattern是list时，new_pattern也要是list，并且二者是等长的，否则报错
                    if isinstance(new_pattern, list):
                        if len(old_pattern) != len(new_pattern):
                            print("Please ensure replace pattern's length equals to original pattern's length")
                            return
                        else:
                            # 如果找到old_pattern在待匹配文件名中，并且new_pattern不在待匹配文件名中（查找new_pattern是否）
                            # 在待匹配文件名中，为了防止多次加入同样的tag
                            if c.find(old_pattern[i]) > -1 and c.find(new_pattern[i]) < 0:
                                new_name = c.replace(old_pattern[i], new_pattern[i])
                                src_path = os.path.join(dir_path, c)
                                dst_path = os.path.join(dir_path, new_name)
                                os.rename(src_path, dst_path)
                    else:
                        if c.find(old_pattern[i]) > -1 and c.find(new_pattern[i]) < 0:
                            new_name = c.replace(old_pattern[i], new_pattern)
                            src_path = os.path.join(dir_path, c)
                            dst_path = os.path.join(dir_path, new_name)
                            os.rename(src_path, dst_path)
            else:
                new_name = c.replace(old_pattern, new_pattern)
                src_path = os.path.join(dir_path, c)
                dst_path = os.path.join(dir_path, new_name)
                os.rename(src_path, dst_path)


def include_exclude_replace(dir_path, pattern, old_pattern, new_pattern, tag=0):
    """
    实现将除（exclude）拥有pattern列表的文件名进行重命名，或者包含(include)pattern的文件进行重命名
    :param dir_path: 重命名文件的文件夹，绝对路径
    :param pattern: 若文件名中包含该字符串，tag=0，该文件名会被修改，tag=1该文件名不会被修改
    :param old_pattern: 待匹配的原始字符串
    :param new_pattern: 匹配成功后修改的字符串
    :param tag: tag=0执行include操作，tag=1执行exclude操作
    :return:
    """
    child_name = os.listdir(dir_path)
    temp_name = child_name.copy()
    flag = 0  # 标志位，判断当前文件名中是否包含patten，flag=0不包括，flag=1包括
    for c in child_name:
        flag = 0
        if os.path.isfile(os.path.join(dir_path, c)):
            if isinstance(pattern, list):
                for ex in pattern:
                    if c.find(ex) > -1:
                        flag = 1
                        break
                if tag == 0:
                    if flag == 0:
                        temp_name.remove(c)
                elif tag == 1:
                    if flag == 1:
                        temp_name.remove(c)
            else:
                if tag == 1:
                    if c.find(pattern) > -1:
                        # 若文件名中包含pattern将该文件名移除,并且当前执行exclude操作
                        temp_name.remove(c)
                elif tag == 0:
                    if c.find(pattern) < 0:
                        # 若文件名中不包含pattern将该文件名移除，并且当前执行include操作
                        temp_name.remove(c)
    do_replace(dir_path, temp_name, old_pattern, new_pattern)


def replace_tag(dir_path, old_pattern, new_pattern):
    """
    :param dir_path: 重命名文件的文件夹，绝对路径
    :param old_pattern: 待匹配的原始字符串
    :param new_pattern: 匹配成功后修改的字符串
    """
    child_file = os.listdir(dir_path)
    do_replace(dir_path, child_file, old_pattern, new_pattern)


def get_suffix(name):
    """
    获取name的后缀
    :param name: 文件名
    :return: 文件名的后缀
    """
    name = str(name)
    name_list = name.split('.')
    return str(name_list[len(name_list) - 1])


def unify_name(dir_path, name):
    """
    该函数实现将文件夹内的文件统一命名为name-序号.后缀
    :param dir_path: 文件目录结对路径
    :param name: 统一命名
    :return:
    """
    child_name = os.listdir(dir_path)
    index = 0
    for c in child_name:
        if os.path.isfile(os.path.join(dir_path, c)):
            src = os.path.join(dir_path, c)
            suffix = get_suffix(c)
            dst = os.path.join(dir_path, name + '-' + index.__str__() + '.' + suffix)
            os.rename(src, dst)
            index += 1


def add_tag(dir_path, tag, head=1):
    """
    实现为名字在头部或尾部加入标记
    :param dir_path: 重命名文件的文件夹，绝对路径
    :param tag: 带加入的tag字符
    :param head: head=0表示在尾部添加，head=1表示在头部添加
    """
    child_file = os.listdir(dir_path)
    for c in child_file:
        if os.path.isfile(os.path.join(dir_path, c)):
            if head == 1:
                new_name = tag + c
            else:
                new_name = c.replace('.', tag + '.')
            src_path = os.path.join(dir_path, c)
            dst_path = os.path.join(dir_path, new_name)
            os.rename(src_path, dst_path)


def remove_tag(dir_path, tag):
    """
    实现将文件名中的tag移除
    :param dir_path: 文件的父目录绝对路径
    :param tag: 待删除tag
    """
    child_file = os.listdir(dir_path)
    for c in child_file:
        if os.path.isfile(os.path.join(dir_path, c)) and c.find(tag) > -1:
            new_name = c.replace(tag, '')
            src_path = os.path.join(dir_path, c)
            dst_path = os.path.join(dir_path, new_name)
            os.rename(src_path, dst_path)


def list_files(dir_path):
    """
    显示所有的dir_path文件夹下的文件名
    :param dir_path: 文件夹的绝对路径
    """
    child_file = os.listdir(dir_path)
    for c in child_file:
        if os.path.isfile(os.path.join(dir_path, c)):
            print(c)


if __name__ == '__main__':
    DIR_PATH = r'C:\Users\磊\Desktop\实验六 报文'
    # DIR_PATH = r'C:\Users\磊\Desktop\新建文件夹'
    # add_str = '-ZY1606408'
    # OLD_PATTERN = '文本'
    # NEW_PATTERN = '图片'  # , '-ZY1606408.'
    # replace_tag(DIR_PATH, OLD_PATTERN, NEW_PATTERN)
    # remove_tag(dir_path, add_str)
    # add_tag(dir_path, add_str, head=0)
    replace_tag(DIR_PATH, '18b', "18B")
    # unify_name(DIR_PATH, '图片')
    # include_exclude_replace(DIR_PATH, ['tcprtodata', 'tcpsndwnddata'], 'ZY1606408', '-ZY1606408', tag=0)
    list_files(DIR_PATH)
    pass

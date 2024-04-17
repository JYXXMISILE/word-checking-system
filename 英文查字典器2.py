while True:
      # 搜索英文段落中的指定词语
     user_input = input("请输入你需要查询的英文段落: ")

     user_list = user_input.split()
     # 创建列表
     target = input("请输入你想寻找的单词: ")
     # 输入要搜索元素

     def linear_search(target, user_list):
        for i, word in enumerate(user_list):
            if word == target:
              return i  # 找到单词，返回其位置
        return -1  # 未找到单词，返回-1

     position = linear_search(target, user_list)
     #  用函数在列表中寻找元素

     if position != -1:
        print(f"找到单词 '{target}' 在句子中的第 {position + 1} 位。")
     else:
        print(f"并未在句子中找到 '{target}'。")
    # 给用户进行反馈
     run_again = input("是否查询下一个句子？（y/n）：")
     if run_again.lower() != "y":
          break
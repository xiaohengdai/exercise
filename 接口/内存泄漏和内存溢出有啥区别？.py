#内存泄漏和内存溢出有啥区别？：https://blog.csdn.net/zhanduo0118/article/details/118937567
# 1、内存泄漏(Memory Leak)：是指程序在申请内存后，无法释放已申请的内存空间，一次内存泄漏似乎不会有大的影响，但内存泄漏堆积后的后果就是内存溢出。
# 2、内存溢出(Memory Overflow)：指程序申请内存时，没有足够的内存供申请者使用，或者说，给了你一块存储int类型数据的存储空间，但是你却存储long类型的数据，那么结果就是内存不够用，此时就会报错OOM,即所谓的内存溢出。

RN质量保障怎么做的？
1、前期调研（RN的相关文档，以及其他部门踩的坑，了解现有的RN基建，）
2、流程规范（比如RN的需求管理规范，涉及到其它组的RN改造对我们这边造成的影响，或者我们这边对其它业务RN的影响，缺陷管理规范，发布规范）
3、RN包的可测性（RN在自动化时的控件定位自动加id；testflight包和v_release包上上报相关RN页面的信息）
4、RN的工具提效
5、RN的监控
6、RN的质量数据运营

大方向:

测试左移:

需求前期阶段: 1、测试对需求的理解 2、需求是否合理 3、需求文档是否完整

需求测试阶段: 1、开发是否进过自测 2、提测打回规范 3、测试用例的设计是什么?  4、测试用例评审 5、是否有showcase 6、测试前是否产品验收 7、测试方案是什么?

8、需求是否符合上车标准?  9、提交bug的规范是什么?  10、是否有每日测试情况同步会

集成阶段: 1、集成回归用例覆盖设计及探索性测试  2、集成阶段前bug闭环 3、集成准出的标准是什么? 4、集成阶段合并MR规范是什么?


测试右移:

灰度阶段: 1、灰度阶段测试用例覆盖设计 2、灰度监控(业务核心指标 + crash类 + 用户反馈)  2、灰度修复问题把控(什么样的MR能在灰度修复,规范是什么)    

全量阶段: 1、线上监控  2、项目复盘(知识沉淀 + badcase总结)
import http from "../utils/http";
import {reactive, ref} from "vue"


const course = reactive({
    current_direction: 0,  // 当前选中的学习方向，0表示所有方向
    current_category: 0,  // 当前选中的课程分类，0表示不限分类
    direction_list: [],    // 学习方向列表
    category_list: [],    // 课程分类列表
    ordering: "",       // 课程排序条件
    page: 1,               // 当前页码，默认为1
    size: 5,               // 当前页数据量
    count: 0,         // 课程信息列表的数量
    has_perv: false,  // 是否有上一页
    has_next: false,  // 是否有下一页
    timer: null,      // 课程相关数据的定时器
    get_course_direction(){
        // 获取学习方向信息
        return http.get("/courses/directions/")
    },
    get_course_category () {
        // 获取课程分类信息
        return http.get(`/courses/categories/${this.current_direction}/`)
    },
    get_course_list () {
        // 获取课程列表信息
        let params = {
          page: this.page,
          size: this.size,
        }
        if(this.ordering){
            params.ordering = this.ordering;
        }
      return http.get(`/courses/${this.current_direction}/${this.current_category}/`, {
          params,
      })
    }
})

export default course;
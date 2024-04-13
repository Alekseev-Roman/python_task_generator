import axios from "axios";
import {saveAs} from "file-saver";

export const downloadTaskByID = async (task: any) => {
    return await axios
        .get(`/backend/export-task?id=${task.task_id}`, {responseType: 'blob'})
        .then(response => {saveAs(response.data, 'task.xml')})
}

export const downloadVariantByID = async (
    task_1: any, task_2: any, task_3: any) => {
    return await axios
        .get(`/backend/export-variant?id-1=${task_1.task_id}&id-2=${task_2.task_id}&id-3=${task_3.task_id}`, {responseType: 'blob'})
        .then(response => {saveAs(response.data, 'variant.zip')})
}

export const fetchVariant = async (params: any) => {
    const data = await axios
        .get(`/backend/generate-variant?type-1=${params[0].type}
        &topic-1=${params[0].topic}&difficulty-1=${params[0].difficulty}
        &type-2=${params[1].type}&topic-2=${params[1].topic}
        &difficulty-2=${params[1].difficulty}&type-3=${params[2].type}
        &topic-3=${params[2].topic}&difficulty-3=${params[2].difficulty}`)
    return data.data
}

export const fetchQuantityTask = async (
    type_id: any, topic_id: any, difficulty: any)=> {
    const data = await axios
        .get(`/backend/get-quantity-tasks?type=${type_id}
        &difficulty=${difficulty}&topic=${topic_id}`)
    return data.data
}


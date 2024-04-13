import axios from "axios";
import {saveAs} from "file-saver";

export const fetchTask =
    async (type_id: any, topic_id: any, difficulty: any) => {
    const data = await axios
        .get(`/backend/generate-task?type=${type_id}
        &difficulty=${difficulty}&topic=${topic_id}`)
    return data.data
}

export const fetchQuantityTask =
    async (type_id: any, topic_id: any, difficulty: any)=> {
    const data = await axios
        .get(`/backend/get-quantity-tasks?type=${type_id}
        &difficulty=${difficulty}&topic=${topic_id}`)
    return data.data
}

export const downloadTaskByID = async (task: any) => {
    return await axios
        .get(`/backend/export-task?id=${task.task_id}`, {responseType: 'blob'})
        .then(response => {saveAs(response.data, 'task.xml')})
}

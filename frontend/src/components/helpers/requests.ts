import axios from "axios";
import {Topic} from "@/types/task";

const adaptTopicsFromServer = (data: any) => {
    const topics: Topic[] = []
    for (const topic in data) {
        topics.push({
            _id: topic,
            name: data[topic]
        })
    }

    return topics
}

export const fetchTopicAll = async () => {
    const data = await axios
        .get('/backend/get-topics')
    return adaptTopicsFromServer(data.data)
}
import axios from "axios";
import {Coderunner, Topic} from "@/types/task";

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

const adaptCoderunnersFromServer = (data: any) => {
    const coderunners: Coderunner[] = []
    for (const coderunner in data) {
        coderunners.push({
            _id: coderunner,
            name: data[coderunner]
        })
    }
    return coderunners
}

export const fetchTopicAll = async () => {
    const data = await axios
        .get('/backend/get-topics')
    return adaptTopicsFromServer(data.data)
}

export const fetchCoderunnerAll = async () => {
    const data = await axios
        .get('/backend/get-coderunners')
    return adaptCoderunnersFromServer(data.data)
}
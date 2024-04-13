"use strict";(self["webpackChunkpygenerator"]=self["webpackChunkpygenerator"]||[]).push([[741],{1741:function(t,e,s){s.r(e),s.d(e,{default:function(){return ct}});var a=function(){var t=this,e=t._self._c;t._self._setupProxy;return e("div",{staticClass:"container justify-content-center align-middle"},[e("div",{staticClass:"h-100 align-middle"},[e("p",{staticClass:"title-1 text-center bold mt-1"},[t._v(" Добавление задачи ")]),e("hr",{staticClass:"hr-1",attrs:{align:"center",size:"4"}}),e("b-card",{staticClass:"text-center"},[e("form",{staticClass:"container-vs text-center",on:{submit:function(e){return e.preventDefault(),t.submitForm.apply(null,arguments)}}},[e("div",{staticClass:"d-flex flex-grow-1 justify-content-between mt-3"},[e("span",{staticClass:"title-2"},[t._v("Сложность")]),t._l(t.difficulties,(function(s){return e("div",{key:s._id,staticClass:"form-check ml-5"},[e("input",{directives:[{name:"model",rawName:"v-model",value:t.selectedDifficulties,expression:"selectedDifficulties"}],staticClass:"form-check-input",attrs:{type:"radio",name:"radioDifficulty",id:"radioDifficulty1",required:""},domProps:{value:s.difficulty,checked:t._q(t.selectedDifficulties,s.difficulty)},on:{change:[function(e){t.selectedDifficulties=s.difficulty},t.getQuantityTasks]}}),e("label",{staticClass:"form-check-label title-2",attrs:{for:"radioDifficulty1"}},[t._v(" "+t._s(s.difficulty)+" ")])])}))],2),e("div",{staticClass:"d-flex flex-grow-1 justify-content-between mt-3"},[e("span",{staticClass:"title-2"},[t._v("Тема")]),e("select",{directives:[{name:"model",rawName:"v-model",value:t.selectedTopic,expression:"selectedTopic"}],staticClass:"form-select ml-5",attrs:{required:""},on:{change:[function(e){var s=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.selectedTopic=e.target.multiple?s:s[0]},t.getQuantityTasks]}},t._l(t.topicList,(function(s){return e("option",{key:s._id,domProps:{value:s._id}},[t._v(t._s(s.name))])})),0)]),e("div",{staticClass:"text-right mt-2",on:{click:function(e){return t.$bvModal.show("add-new-topic")}}},[e("button",{staticClass:"act-button text-white",attrs:{type:"button"}},[t._v(" Новая тема ")])]),e("div",{staticClass:"d-flex flex-grow-1 justify-content-left mt-3"},[e("span",{staticClass:"text mr-3"},[t._v("Средняя уникальность подходящих задач: ")]),e("span",{class:[t.task_match.mathPercent<60?"red-text":"text"]},[t._v(" "+t._s(t.task_match.mathPercent)+" % ")])]),e("div",{staticClass:"d-flex flex-grow-1 justify-content-left mt-3"},[e("span",{staticClass:"text mr-3"},[t._v("Количество подходящих задач в теме: ")]),e("span",{class:[t.quantityTasks<1?"red-text":"text"]},[t._v(" "+t._s(t.quantityTasks)+" ")])]),e("div",{staticClass:"mt-3"},[t.selectedDifficulties&&t.selectedTopic?e("input",{attrs:{id:"importFile",type:"file",hidden:"",accept:".xml"},on:{change:t.importFile}}):t._e(),e("button",{directives:[{name:"b-tooltip",rawName:"v-b-tooltip"}],staticClass:"custom-button text",attrs:{type:"submit"},on:{click:t.download}},[t._v("Загрузить файл ")]),e("button",{staticClass:"ml-2 custom-button text",attrs:{type:"submit"},on:{click:function(e){t.selectedDifficulties&&t.selectedTopic&&t.$bvModal.show("add-by-url"),t.creating=!1}}},[t._v(" Загрузить по ссылке ")]),e("button",{staticClass:"ml-2 custom-button text",attrs:{type:"submit"},on:{click:function(e){t.selectedDifficulties&&t.selectedTopic&&(t.creating=!0)}}},[t._v("Создать задачу")])])])]),t.creating?e("div",[e("CreateNew")],1):t._e()],1),e("AddByUrl"),e("AddNewTopic")],1)},i=[],l=s(6318),c=s(1929),n=function(){var t=this,e=t._self._c;t._self._setupProxy;return e("b-modal",{attrs:{title:"Добавление по ссылке",id:"add-by-url",centered:""},on:{cancel:t.cancel,close:t.cancel},scopedSlots:t._u([{key:"modal-footer",fn:function({ok:s,cancel:a}){return[e("b-button",{staticClass:"custom-button small mr-3 text",attrs:{variant:"primary"},on:{click:a}},[t._v(" Отмена ")]),e("b-button",{staticClass:"custom-button text",attrs:{variant:"primary"},on:{click:s}},[t._v(" Добавить ")])]}}])},[e("div",{staticClass:"form-group"},[e("label",{staticClass:"title-2",attrs:{for:"inputTaskUrl"}},[t._v(" Введите ссылку на задачу ")]),e("input",{directives:[{name:"model",rawName:"v-model",value:t.taskUrl,expression:"taskUrl"}],staticClass:"form-control",attrs:{type:"text","aria-describedby":"emailHelp",placeholder:"https://e.moevm.info/question/question.php"},domProps:{value:t.taskUrl},on:{input:function(e){e.target.composing||(t.taskUrl=e.target.value)}}})])])},r=[],o=function(t,e,s,a){var i,l=arguments.length,c=l<3?e:null===a?a=Object.getOwnPropertyDescriptor(e,s):a;if("object"===typeof Reflect&&"function"===typeof Reflect.decorate)c=Reflect.decorate(t,e,s,a);else for(var n=t.length-1;n>=0;n--)(i=t[n])&&(c=(l<3?i(c):l>3?i(e,s,c):i(e,s))||c);return l>3&&c&&Object.defineProperty(e,s,c),c};let u=class extends c.w3{constructor(...t){super(...t),(0,l.Z)(this,"taskUrl","")}async cancel(){}};u=o([(0,c.wA)({})],u);var d=u,f=d,p=s(1001),m=(0,p.Z)(f,n,r,!1,null,"52c3938d",null),v=m.exports,_=function(){var t=this,e=t._self._c;t._self._setupProxy;return e("div",{staticClass:"container justify-content-center align-middle mt-3"},[e("div",{staticClass:"h-100 align-middle"},[e("b-card",{staticClass:"text-center"},[e("div",{staticClass:"mt-3 d-flex flex-grow-1 justify-content-between"},[e("span",{staticClass:"title-2"},[t._v("Тип")]),e("select",{directives:[{name:"model",rawName:"v-model",value:t.selectedType,expression:"selectedType"}],staticClass:"form-select ml-5",on:{change:function(e){var s=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.selectedType=e.target.multiple?s:s[0]}}},t._l(t.types,(function(s){return e("option",{key:s._id,domProps:{value:s._id}},[t._v(t._s(s.type))])})),0)]),1==t.selectedType?e("div",[e("NewCoderunnerTaskCard")],1):t._e(),2==t.selectedType?e("div",[e("NewMultichoiceTaskCard")],1):t._e()])],1)])},h=[],x=s(5567),y=function(){var t=this,e=t._self._c;t._self._setupProxy;return e("div",[t._m(0),e("div",{staticClass:"d-flex flex-grow-1 justify-content-left mt-3"},[e("label",{staticClass:"text"},[t._v("Количество правильных ответов ")]),t._l(t.answerNumbers,(function(s){return e("div",{key:s._id,staticClass:"form-check ml-5"},[e("input",{directives:[{name:"model",rawName:"v-model",value:t.selectedAnswerNumber,expression:"selectedAnswerNumber"}],staticClass:"form-check-input",attrs:{type:"radio",name:"radioDifficulty",id:"radioDifficulty1"},domProps:{value:s.number,checked:t._q(t.selectedAnswerNumber,s.number)},on:{change:function(e){t.selectedAnswerNumber=s.number}}}),e("label",{staticClass:"form-check-label title-2",attrs:{for:"radioDifficulty1"}},[t._v(" "+t._s(s.number)+" ")])])}))],2),e("div",{staticClass:"text-left mt-3"},[t._m(1),t._l(t.answers,(function(s){return e("b-card",{key:s._id,staticClass:"mt-3"},[e("label",{staticClass:"text"},[t._v("Вариант ответа")]),e("textarea",{staticClass:"form-control",attrs:{rows:"2"}}),e("div",{staticClass:"mt-3 d-flex flex-grow-1 justify-content-between"},[e("div",{staticClass:"text-left"},[e("label",{staticClass:"text"},[t._v("Оценка")]),e("input",{staticClass:"ml-5",attrs:{type:"number",id:"grade",name:"grade",min:"-100",max:"100"}}),e("span",{staticClass:"text ml-2"},[t._v("%")])]),e("button",{staticClass:"custom-button act-button w-text w-15",on:{click:function(e){return t.deleteAnswer(s)}}},[t._v(" Удалить ")])])])})),e("div",[e("button",{staticClass:"custom-button act-button w-text mt-3 w-25",on:{click:t.newAnswer}},[t._v(" Добавить вариант ответа ")])])],2),t._m(2)])},w=[function(){var t=this,e=t._self._c;t._self._setupProxy;return e("div",{staticClass:"text-left mt-3"},[e("label",{staticClass:"text"},[t._v("Условие")]),e("textarea",{staticClass:"form-control",attrs:{rows:"7"}})])},function(){var t=this,e=t._self._c;t._self._setupProxy;return e("div",[e("label",{staticClass:"text"},[t._v("Варианты ответа")])])},function(){var t=this,e=t._self._c;t._self._setupProxy;return e("div",{staticClass:"mt-3 d-flex flex-grow-1 justify-content-left"},[e("button",{staticClass:"custom-button act-button w-text mt-3 w-25"},[t._v(" Сохранить ")])])}],b=(s(560),function(t,e,s,a){var i,l=arguments.length,c=l<3?e:null===a?a=Object.getOwnPropertyDescriptor(e,s):a;if("object"===typeof Reflect&&"function"===typeof Reflect.decorate)c=Reflect.decorate(t,e,s,a);else for(var n=t.length-1;n>=0;n--)(i=t[n])&&(c=(l<3?i(c):l>3?i(e,s,c):i(e,s))||c);return l>3&&c&&Object.defineProperty(e,s,c),c});let C=class extends c.w3{constructor(...t){super(...t),(0,l.Z)(this,"answerNumbers",x.N1),(0,l.Z)(this,"selectedAnswerNumber",0),(0,l.Z)(this,"answers",[])}newAnswer(){this.answers.push({_id:0==this.answers.length?0:this.answers[this.answers.length-1]._id+1,answer:"",answer_fraction:0})}deleteAnswer(t){this.answers.splice(this.answers.indexOf(t),1)}};C=b([(0,c.wA)({})],C);var g=C,k=g,T=(0,p.Z)(k,y,w,!1,null,"6b50e8c4",null),N=T.exports,A=function(){var t=this,e=t._self._c;t._self._setupProxy;return e("div",[e("div",{staticClass:"mt-3 d-flex flex-grow-1 justify-content-between"},[e("label",{staticClass:"title-2"},[t._v("Тип coderunner ")]),e("select",{directives:[{name:"model",rawName:"v-model",value:t.selectedCoderunnerType,expression:"selectedCoderunnerType"}],staticClass:"form-select ml-5",on:{change:function(e){var s=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.selectedCoderunnerType=e.target.multiple?s:s[0]}}},t._l(t.coderunnerTypes,(function(s){return e("option",{key:s._id,domProps:{value:s._id}},[t._v(" "+t._s(s.name)+" ")])})),0)]),t._m(0),t._m(1),t._m(2),e("div",{staticClass:"text-left mt-3"},[t._m(3),t._l(t.answers,(function(s){return e("b-card",{key:s._id,staticClass:"mt-3"},[e("label",{staticClass:"text"},[t._v("Пример")]),e("textarea",{directives:[{name:"model",rawName:"v-model",value:s.example,expression:"answer.example"}],staticClass:"form-control",attrs:{rows:"5"},domProps:{value:s.example},on:{input:function(e){e.target.composing||t.$set(s,"example",e.target.value)}}}),e("label",{staticClass:"text"},[t._v("Ввод")]),e("textarea",{directives:[{name:"model",rawName:"v-model",value:s.input,expression:"answer.input"}],staticClass:"form-control",attrs:{rows:"5"},domProps:{value:s.input},on:{input:function(e){e.target.composing||t.$set(s,"input",e.target.value)}}}),e("label",{staticClass:"text"},[t._v("Результат")]),e("textarea",{directives:[{name:"model",rawName:"v-model",value:s.result,expression:"answer.result"}],staticClass:"form-control",attrs:{rows:"5"},domProps:{value:s.result},on:{input:function(e){e.target.composing||t.$set(s,"result",e.target.value)}}}),e("div",{staticClass:"mt-3 d-flex flex-grow-1 justify-content-between"},[e("div",{staticClass:"mt-3 d-flex flex-grow-1 justify-content-left"},[e("span",{staticClass:"title-2"},[t._v("Использовать как пример ")]),e("input",{directives:[{name:"model",rawName:"v-model",value:s.use_as_example,expression:"answer.use_as_example"}],staticClass:"form-check ml-3",attrs:{type:"checkbox",name:"checkboxUseAsExample",id:"checkboxUseAsExample"},domProps:{checked:Array.isArray(s.use_as_example)?t._i(s.use_as_example,null)>-1:s.use_as_example},on:{change:function(e){var a=s.use_as_example,i=e.target,l=!!i.checked;if(Array.isArray(a)){var c=null,n=t._i(a,c);i.checked?n<0&&t.$set(s,"use_as_example",a.concat([c])):n>-1&&t.$set(s,"use_as_example",a.slice(0,n).concat(a.slice(n+1)))}else t.$set(s,"use_as_example",l)}}})]),e("button",{staticClass:"custom-button act-button w-text w-15",on:{click:function(e){return t.deleteAnswer(s)}}},[t._v(" Удалить ")])])])})),e("div",[e("button",{staticClass:"custom-button act-button w-text mt-3 w-25",on:{click:t.newAnswer}},[t._v(" Добавить тестовый пример ")])])],2),t._m(4)])},P=[function(){var t=this,e=t._self._c;t._self._setupProxy;return e("div",{staticClass:"text-left mt-3"},[e("label",{staticClass:"text"},[t._v("Условие")]),e("textarea",{staticClass:"form-control",attrs:{rows:"7"}})])},function(){var t=this,e=t._self._c;t._self._setupProxy;return e("div",{staticClass:"text-left mt-3"},[e("label",{staticClass:"text"},[t._v("Заполнение шаблона")]),e("textarea",{staticClass:"form-control",attrs:{rows:"5"}})])},function(){var t=this,e=t._self._c;t._self._setupProxy;return e("div",{staticClass:"text-left mt-3"},[e("label",{staticClass:"text"},[t._v("Код проверки")]),e("textarea",{staticClass:"form-control",attrs:{rows:"12"}})])},function(){var t=this,e=t._self._c;t._self._setupProxy;return e("div",[e("label",{staticClass:"text"},[t._v("Тестовые примеры")])])},function(){var t=this,e=t._self._c;t._self._setupProxy;return e("div",{staticClass:"mt-3 d-flex flex-grow-1 justify-content-left"},[e("button",{staticClass:"custom-button act-button w-text mt-3 w-25"},[t._v(" Сохранить ")])])}],j=function(t,e,s,a){var i,l=arguments.length,c=l<3?e:null===a?a=Object.getOwnPropertyDescriptor(e,s):a;if("object"===typeof Reflect&&"function"===typeof Reflect.decorate)c=Reflect.decorate(t,e,s,a);else for(var n=t.length-1;n>=0;n--)(i=t[n])&&(c=(l<3?i(c):l>3?i(e,s,c):i(e,s))||c);return l>3&&c&&Object.defineProperty(e,s,c),c};let Z=class extends c.w3{constructor(...t){super(...t),(0,l.Z)(this,"selectedCoderunnerType",null),(0,l.Z)(this,"coderunnerTypes",[]),(0,l.Z)(this,"answers",[])}newAnswer(){this.answers.push({_id:0==this.answers.length?0:this.answers[this.answers.length-1]._id+1,example:"",input:"",result:"",use_as_example:!1})}deleteAnswer(t){this.answers.splice(this.answers.indexOf(t),1)}};Z=j([(0,c.wA)({})],Z);var D=Z,R=D,O=(0,p.Z)(R,A,P,!1,null,"47cc5a3c",null),U=O.exports,q=function(t,e,s,a){var i,l=arguments.length,c=l<3?e:null===a?a=Object.getOwnPropertyDescriptor(e,s):a;if("object"===typeof Reflect&&"function"===typeof Reflect.decorate)c=Reflect.decorate(t,e,s,a);else for(var n=t.length-1;n>=0;n--)(i=t[n])&&(c=(l<3?i(c):l>3?i(e,s,c):i(e,s))||c);return l>3&&c&&Object.defineProperty(e,s,c),c};let $=class extends c.w3{constructor(...t){super(...t),(0,l.Z)(this,"selectedType",0),(0,l.Z)(this,"types",x.V5),(0,l.Z)(this,"topicList",[]),(0,l.Z)(this,"task",[])}};$=q([(0,c.wA)({components:{NewCoderunnerTaskCard:U,NewMultichoiceTaskCard:N}})],$);var F=$,L=F,M=(0,p.Z)(L,_,h,!1,null,"901f7620",null),B=M.exports,E=s(5121);const Q=t=>{const e=new FormData;e.append("data",t)},S=async t=>{await E.Z.post(`/backend/import-new-topic?topic=${t}`)},V=async t=>{const e=await E.Z.get(`/backend/check-topic-in-db?topic=${t}`);return e.data},z=async(t,e)=>0;var G=s(8875),H=function(){var t=this,e=t._self._c;t._self._setupProxy;return e("b-modal",{attrs:{title:"Добавление по ссылке",id:"add-new-topic",centered:""},on:{close:t.close,cancel:t.close,ok:t.addTopic},scopedSlots:t._u([{key:"modal-footer",fn:function({ok:s,cancel:a}){return[e("b-button",{staticClass:"custom-button small mr-3 text",attrs:{variant:"primary"},on:{click:a}},[t._v(" Отмена ")]),e("b-button",{staticClass:"custom-button text",attrs:{variant:"primary"},on:{click:function(e){t.canAdd&&s()}}},[t._v(" Добавить ")])]}}])},[e("div",{staticClass:"form-group"},[e("label",{staticClass:"title-2",attrs:{for:"inputTaskUrl"}},[t._v(" Введите название темы ")]),e("input",{directives:[{name:"model",rawName:"v-model",value:t.topicName,expression:"topicName"}],staticClass:"form-control",attrs:{type:"text"},domProps:{value:t.topicName},on:{change:t.checkTopicName,input:function(e){e.target.composing||(t.topicName=e.target.value)}}}),"1"==t.checkingResult?e("label",{staticClass:"red-text mt-2"},[t._v(" Тема с таким названием уже существует ")]):t._e()])])},I=[],J=function(t,e,s,a){var i,l=arguments.length,c=l<3?e:null===a?a=Object.getOwnPropertyDescriptor(e,s):a;if("object"===typeof Reflect&&"function"===typeof Reflect.decorate)c=Reflect.decorate(t,e,s,a);else for(var n=t.length-1;n>=0;n--)(i=t[n])&&(c=(l<3?i(c):l>3?i(e,s,c):i(e,s))||c);return l>3&&c&&Object.defineProperty(e,s,c),c};let K=class extends c.w3{constructor(...t){super(...t),(0,l.Z)(this,"topicName",""),(0,l.Z)(this,"checkingResult","0"),(0,l.Z)(this,"canAdd",!1)}async checkTopicName(){""!=this.topicName&&(this.checkingResult=await V(this.topicName),"0"==this.checkingResult&&(this.canAdd=!0))}async addTopic(){await this.checkTopicName(),"0"==this.checkingResult&&""!=this.topicName&&(await S(this.topicName),this.checkingResult="0",this.topicName="",this.canAdd=!1)}close(){this.checkingResult="0",this.topicName="",this.canAdd=!1}};K=J([(0,c.wA)({})],K);var W=K,X=W,Y=(0,p.Z)(X,H,I,!1,null,"21e42ba4",null),tt=Y.exports,et=function(t,e,s,a){var i,l=arguments.length,c=l<3?e:null===a?a=Object.getOwnPropertyDescriptor(e,s):a;if("object"===typeof Reflect&&"function"===typeof Reflect.decorate)c=Reflect.decorate(t,e,s,a);else for(var n=t.length-1;n>=0;n--)(i=t[n])&&(c=(l<3?i(c):l>3?i(e,s,c):i(e,s))||c);return l>3&&c&&Object.defineProperty(e,s,c),c};let st=class extends c.w3{constructor(...t){super(...t),(0,l.Z)(this,"selectedData",{topic:null,difficulty:null}),(0,l.Z)(this,"types",x.V5),(0,l.Z)(this,"task_match",[]),(0,l.Z)(this,"topicList",[]),(0,l.Z)(this,"creating",!1),(0,l.Z)(this,"quantityTasks",0),(0,l.Z)(this,"difficulties",x.n9),(0,l.Z)(this,"selectedDifficulties",null),(0,l.Z)(this,"selectedTopic",null)}async created(){await this.getAllTopics()}async getAllTopics(){this.topicList=await(0,G.G)()}async getQuantityTasks(){null!=this.selectedTopic&&null!=this.selectedDifficulties&&(this.quantityTasks=await z(this.selectedTopic,this.selectedDifficulties))}importFile(t){Q(t.target.files[0])}download(){this.creating=!1,document.getElementById("importFile")?.click()}async submitForm(){this.selectedData.topic=this.selectedTopic,this.selectedData.difficulty=this.selectedDifficulties}async newTopic(){}};st=et([(0,c.wA)({components:{AddByUrl:v,AddNewTopic:tt,CreateNew:B}})],st);var at=st,it=at,lt=(0,p.Z)(it,a,i,!1,null,"2126d382",null),ct=lt.exports}}]);
//# sourceMappingURL=741.00e6196d.js.map
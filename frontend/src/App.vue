<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const students = ref([])
const loading = ref(false)
const form = ref({ id: null, student_no: '', name: '', gender: 'male', major: '', grade: '', phone: '', email: '' })
const error = ref('')

async function fetchStudents() {
  loading.value = true
  try {
    const { data } = await axios.get('/api/students/')
    students.value = data
  } catch (e) {
    error.value = '加载学生列表失败'
  } finally {
    loading.value = false
  }
}

function resetForm() {
  form.value = { id: null, student_no: '', name: '', gender: 'male', major: '', grade: '', phone: '', email: '' }
}

async function saveStudent() {
  try {
    if (form.value.id) {
      await axios.put(`/api/students/${form.value.id}/`, form.value)
    } else {
      await axios.post('/api/students/', { ...form.value, grade: form.value.grade ? Number(form.value.grade) : null })
    }
    await fetchStudents()
    resetForm()
  } catch (e) {
    error.value = '保存失败，请检查输入'
  }
}

async function editStudent(s) {
  form.value = { ...s }
}

async function deleteStudent(id) {
  if (!confirm('确定删除该学生吗？')) return
  await axios.delete(`/api/students/${id}/`)
  await fetchStudents()
}

onMounted(fetchStudents)
</script>

<template>
  <div style="max-width: 900px; margin: 24px auto; font-family: system-ui, sans-serif;">
    <h2>大学生管理系统</h2>
    <div v-if="error" style="color: #c00; margin-bottom: 12px;">{{ error }}</div>

    <form @submit.prevent="saveStudent" style="display:grid; grid-template-columns: repeat(3, 1fr); gap:12px; align-items:end; border:1px solid #eee; padding:16px; border-radius:8px;">
      <div>
        <label>学号</label>
        <input v-model="form.student_no" required placeholder="如 20250001" style="width:100%" />
      </div>
      <div>
        <label>姓名</label>
        <input v-model="form.name" required style="width:100%" />
      </div>
      <div>
        <label>性别</label>
        <select v-model="form.gender" style="width:100%">
          <option value="male">男</option>
          <option value="female">女</option>
        </select>
      </div>
      <div>
        <label>专业</label>
        <input v-model="form.major" style="width:100%" />
      </div>
      <div>
        <label>年级</label>
        <input v-model="form.grade" type="number" min="2000" max="2100" style="width:100%" />
      </div>
      <div>
        <label>电话</label>
        <input v-model="form.phone" style="width:100%" />
      </div>
      <div>
        <label>邮箱</label>
        <input v-model="form.email" type="email" style="width:100%" />
      </div>
      <div>
        <button type="submit" style="padding:8px 12px;">{{ form.id ? '更新' : '添加' }}</button>
        <button type="button" @click="resetForm" style="padding:8px 12px; margin-left:8px;">重置</button>
      </div>
    </form>

    <div style="margin-top:16px; display:flex; justify-content:space-between; align-items:center;">
      <strong>学生列表</strong>
      <button @click="fetchStudents" :disabled="loading">{{ loading ? '刷新中…' : '刷新' }}</button>
    </div>

    <table border="1" cellspacing="0" cellpadding="8" style="width:100%; margin-top:8px; border-collapse:collapse;">
      <thead>
        <tr>
          <th>ID</th>
          <th>学号</th>
          <th>姓名</th>
          <th>性别</th>
          <th>专业</th>
          <th>年级</th>
          <th>电话</th>
          <th>邮箱</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="s in students" :key="s.id">
          <td>{{ s.id }}</td>
          <td>{{ s.student_no }}</td>
          <td>{{ s.name }}</td>
          <td>{{ s.gender === 'male' ? '男' : '女' }}</td>
          <td>{{ s.major }}</td>
          <td>{{ s.grade }}</td>
          <td>{{ s.phone }}</td>
          <td>{{ s.email }}</td>
          <td>
            <button @click="editStudent(s)">编辑</button>
            <button style="margin-left:8px;" @click="deleteStudent(s.id)">删除</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
label { display:block; margin-bottom:4px; font-size:12px; color:#555 }
input, select { height:32px; padding:4px 8px; border:1px solid #ccc; border-radius:4px }
button { cursor:pointer }
</style>

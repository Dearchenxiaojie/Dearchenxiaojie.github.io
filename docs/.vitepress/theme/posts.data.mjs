import { createContentLoader } from 'vitepress'

export default createContentLoader('posts/*.md', {
  excerpt: true,
  transform(rawData) {
    return rawData
      .map(({ url, frontmatter, excerpt }) => ({
        title: frontmatter.title || '无标题',
        description: frontmatter.description || excerpt?.slice(0, 100) || '',
        date: formatDate(frontmatter.date),
        readingTime: Math.max(1, Math.ceil((excerpt?.length || 0) / 500)),
        url,
        tags: frontmatter.tags || [],
        cover: frontmatter.cover || ''
      }))
      .sort((a, b) => new Date(b.date) - new Date(a.date))
  }
})

function formatDate(date) {
  if (!date) return '未知日期'
  const d = new Date(date)
  return `${d.getFullYear()}.${String(d.getMonth() + 1).padStart(2, '0')}.${String(d.getDate()).padStart(2, '0')}`
}

export const data = []

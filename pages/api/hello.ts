// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'

type Data = {
  name: string |string[]
}

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  if(req.method != 'GET') return res.status(400).json({name: "Requisição HTTP inválida"})
  res.status(200).json({ name: req.query.nome, date })
}

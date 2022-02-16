import React from 'react'
import { graphql } from 'gatsby'

import Layout from '../components/layout'
import { Link } from '../components/link'
import Logo from '../../static/logo.svg'

import classes from '../styles/index.module.sass'

export default ({ data }) => {
    const siteMetadata = data.site.siteMetadata
    const chapters = data.allMarkdownRemark.edges.map(({ node }) => ({
        slug: node.fields.slug,
        title: node.frontmatter.title,
        description: node.frontmatter.description,
    }))
    return (
        <Layout isHome>
            <Logo className={classes.logo} aria-label={siteMetadata.title} />
            <section>

                <h1 className={classes.subtitle}><center>Welcome to EarthCube Interactive Workshops!</center></h1>
                <div className={classes.introduction}>
                <p></p>

                <center>
                <p>
                    These short courses will teach you how to conduct reproducible 
                    research using Data Sciences tools.  

                    You will be working with Python, Jupyter, Docker containerization,
                    and Git for version control.  

                </p>
                <p>
                    After these modules, you will be able to process your own research
                    in a format suitable for analysis, writing your own analysis functions,
                    and deriving data-driven insights via Jupyter Notebooks and RMarkdown files.
                </p>
                <p>
                    This page runs on a python3 kernel.
                    To visit the R kernel version, click <a href="https://throughput-ec.github.io/ec-workshops/" target="_blank" >here</a>.

                </p>
                </center>
                </div>
            </section>
            {chapters.map(({ slug, title, description }) => (
                <section key={slug} className={classes.chapter}>
                    <h2 className={classes.chapterTitle}>
                        <Link hidden to={slug}>
                            {title}
                        </Link>
                    </h2>
                    <p className={classes.chapterDesc}>
                        <Link hidden to={slug}>
                            {description}
                        </Link>
                    </p>
                </section>
            ))}
        </Layout>
    )
}

export const pageQuery = graphql`
    {
        site {
            siteMetadata {
                title
            }
        }
        allMarkdownRemark(
            sort: { fields: [frontmatter___title], order: ASC }
            filter: { frontmatter: { type: { eq: "chapter" } } }
        ) {
            edges {
                node {
                    fields {
                        slug
                    }
                    frontmatter {
                        title
                        description
                    }
                }
            }
        }
    }
`
